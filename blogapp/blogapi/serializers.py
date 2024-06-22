from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from blogapp.models import (Post,
                            Comment,
                            Like)


class SignUpSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    def create(self, validated_data):
        username = validated_data['email']
        if username:
            validated_data['username'] = username
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def validate(self, data):
        email = data['email']
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email_error': 'email_already_registered'})
        return data


class CreatePostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)

    def create(self, validated_data):
        user_id = self.context['user_id']
        user_obj = User.objects.get(id=user_id)
        return Post.objects.create(user=user_obj, **validated_data)


class CreateShowSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    user_id = serializers.IntegerField()
    published_date = serializers.DateTimeField()


class PatchSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    user_id = serializers.IntegerField(read_only=True)
    published_date = serializers.DateTimeField(read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.title)
        instance.author = validated_data.get('author', instance.title)
        instance.save()
        return instance


class CreateCommentSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=100)
    text = serializers.CharField(max_length=100)

    def create(self, validated_data):
        user_id = self.context['user_id']
        post_id = self.context['post_id']
        user_obj = User.objects.get(id=user_id)
        post_obj = Post.objects.get(id=post_id)
        return Comment.objects.create(user=user_obj, post=post_obj, **validated_data)


class CommentShowSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    post_id = serializers.IntegerField()
    author = serializers.CharField(max_length=100)
    text = serializers.CharField(max_length=100)
    created_date = serializers.DateTimeField()


class CommentPatchSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=100)
    text = serializers.CharField(max_length=100)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance


class PostListWithCommentSerializer(CreateShowSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        comm_obj = Comment.objects.filter(post=instance)
        data['comment'] = CommentShowSerializer(comm_obj, many=True).data
        like_count = Like.objects.filter(post=instance, liked=True).count()
        data['like'] = like_count
        return data


class SinglePostRetreiveWithCommentSerializer(CreateShowSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        comm_obj = Comment.objects.filter(post=instance)
        data['comment'] = CommentShowSerializer(comm_obj, many=True).data
        return data




