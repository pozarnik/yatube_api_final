from datetime import datetime
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination

from posts.models import Group, Post, Comment, Follow
from .permissions import AuthorOrReadOnly
from .serializers import PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthorOrReadOnly]
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, pub_date=datetime.now())


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = PageNumberPagination


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [AuthorOrReadOnly]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, created=datetime.now(), post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, following=serializer.following)

