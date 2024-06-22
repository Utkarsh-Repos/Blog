from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.http import Http404


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import (SignUpSerializer,
                          CreatePostSerializer,
                          CreateShowSerializer,
                          PatchSerializer,
                          CreateCommentSerializer,
                          CommentShowSerializer,
                          CommentPatchSerializer,
                          PostListWithCommentSerializer,
                          SinglePostRetreiveWithCommentSerializer)
from blogapp.models import (Post,
                            Comment,
                            Like)


class SignUpView(APIView):

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class CreatePost(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CreatePostSerializer(data=request.data, context={'user_id': request.user.id})
        if serializer.is_valid():
            instance = serializer.save()
            post_obj = Post.objects.get(id=instance.id)
            serializer_to_show = CreateShowSerializer(post_obj)
            return Response(serializer_to_show.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePost(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        post_obj = Post.objects.filter(id=pk)
        if post_obj.exists():
            if post_obj[0].user.id != request.user.id:
                return Response({'message': 'you are not authorized to edit this post'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                serialized_data = PatchSerializer(post_obj.first(), data=request.data, partial=True)
                if serialized_data.is_valid():
                    instance = serialized_data.save()
                    post_obj = Post.objects.get(id=pk)
                    serializer_to_show = CreateShowSerializer(post_obj)
                    return Response(serializer_to_show.data, status=status.HTTP_200_OK)
                else:
                    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'post not exist regarding same id'}, status=status.HTTP_201_CREATED)


class DeletePost(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        post_obj = Post.objects.filter(id=pk)
        if post_obj.exists():
            if post_obj[0].user.id != request.user.id:
                return Response({'message': 'you are not authorized to delete this post'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                post_obj[0].delete()
                return Response({'message': 'post delete successfully'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'post not exist regarding same id'}, status=status.HTTP_201_CREATED)


class CreateComment(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, post_pk):
        post_obj = Post.objects.filter(id=post_pk)
        if post_obj:
            serializer = CreateCommentSerializer(data=request.data, context={'post_id': post_obj.first().id,
                                                                             'user_id': request.user.id})
            if serializer.is_valid():
                instance = serializer.save()
                comment_obj = Comment.objects.get(id=instance.id)
                serializer_to_show = CommentShowSerializer(comment_obj)
                return Response(serializer_to_show.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'post not exist'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateComment(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        comm_obj = Comment.objects.filter(id=pk)
        if comm_obj.exists():
            if comm_obj[0].user.id != request.user.id:
                return Response({'message': 'you are not authorized to edit this comment'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                serialized_data = CommentPatchSerializer(comm_obj.first(), data=request.data, partial=True)
                if serialized_data.is_valid():
                    instance = serialized_data.save()
                    comm_obj = Comment.objects.get(id=pk)
                    serializer_to_show = CommentShowSerializer(comm_obj)
                    return Response(serializer_to_show.data, status=status.HTTP_200_OK)
                else:
                    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'comment not exist regarding same id'}, status=status.HTTP_201_CREATED)


class DeleteComment(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        comm_obj = Comment.objects.filter(id=pk)
        if comm_obj.exists():
            if comm_obj[0].user.id != request.user.id:
                return Response({'message': 'you are not authorized to delete this comment'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                comm_obj[0].delete()
                return Response({'message': 'post delete successfully'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'post not exist regarding same id'}, status=status.HTTP_201_CREATED)


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'


class PostListWithComment(APIView, CustomPageNumberPagination):

    def get(self, request, format=None):
        post_obj = Post.objects.all()
        results = self.paginate_queryset(post_obj, request, view=self)
        serializer = PostListWithCommentSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)


class SinglePostRetreiveWithComment(APIView):
    def get(self, request, pk):
        post_obj = Post.objects.filter(id=pk)
        if post_obj.exists():
            serializers = SinglePostRetreiveWithCommentSerializer(post_obj.first())
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'no data found with corresponding post id'},
                            status=status.HTTP_204_NO_CONTENT)


class LikePost(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            post = get_object_or_404(Post, id=pk)
        except Http404:
            return Response({'message': 'No data found with corresponding post ID'}, status=status.HTTP_404_NOT_FOUND)

        like_queryset = post.like_set.all().filter(user=request.user)
        if like_queryset.exists():
            like_obj = like_queryset.first()
            if like_obj.liked:
                like_obj.delete()
            else:
                like_obj.liked = True
                like_obj.save()
        else:
            like = Like()
            like.user = request.user
            like.post = post
            like.liked = True
            like.save()
        return Response({'message': 'Like status updated'}, status=status.HTTP_200_OK)
