from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

api_v1_router = DefaultRouter()
api_v1_router.register('posts', PostViewSet, basename='posts')
api_v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
api_v1_router.register(r'groups', GroupViewSet, basename='groups')
api_v1_router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    # адреса, заданные роутером
    path('v1/', include(api_v1_router.urls)),
    # JWT-эндпоинты, для управления JWT-токенами
    path('v1/', include('djoser.urls.jwt')),
]
