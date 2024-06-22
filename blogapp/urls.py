from django.urls import path, include
from . import views

urlpatterns = [
    path("blogapi/", include('blogapp.blogapi.urls')),
]