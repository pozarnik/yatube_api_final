from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'v1/groups', GroupViewSet, basename='group')
router.register(r'v1/posts', PostViewSet, basename='post')
router.register(r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')
router.register(r'v1/follow', FollowViewSet, basename='follower')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('', include(router.urls), name='api-root'),
]
