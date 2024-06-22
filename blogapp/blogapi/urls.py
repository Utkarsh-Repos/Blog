from django.urls import path, include
from .views import (SignUpView,
                    LoginView,
                    CreatePost,
                    UpdatePost,
                    DeletePost,
                    CreateComment,
                    UpdateComment,
                    DeleteComment,
                    PostListWithComment,
                    SinglePostRetreiveWithComment,
                    LikePost)

urlpatterns = [

    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('create-post/', CreatePost.as_view(), name='create-post'),
    path('update-post/<int:pk>/', UpdatePost.as_view(), name='update-post'),
    path('delete-post/<int:pk>/', DeletePost.as_view(), name='delete-post'),
    path('create-comment/<int:post_pk>/', CreateComment.as_view(), name='create-comment'),
    path('update-comment/<int:pk>/', UpdateComment.as_view(), name='update-comment'),
    path('delete-comment/<int:pk>/', DeleteComment.as_view(), name='delete-comment'),
    path('post-list-with-comment-like-count/', PostListWithComment.as_view(), name='post-list-with-comment-like-count'),
    path('single-post-retrieve-with-comment-like-count/<int:pk>/', SinglePostRetreiveWithComment.as_view(),
         name='single-post-retrieve-with-comment-like-count'),
    path('like-post/<int:pk>/', LikePost.as_view(), name='like-post'),




]