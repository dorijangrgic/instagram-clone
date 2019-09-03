from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from instagramcloneapp.serializers import PostSerializer
from .models import Post
from users.models import CustomUser, Follow
from rest_framework import permissions
from rest_framework.response import Response


class PostListPublic(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]


class PostCreate(CreateAPIView):
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostListPrivate(APIView):

    def get(self, request):
        user = request.user
        following = Follow.objects.filter(who_id=user.id)
        queryset = Post.objects.none()

        for f in following:
            posts = Post.objects.filter(author=f.whom_id)
            queryset |= posts

        posts = PostSerializer(queryset, many=True)
        return Response(posts.data)
