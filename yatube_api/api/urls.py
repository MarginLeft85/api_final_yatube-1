from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

api_v1_router = DefaultRouter()
api_v1_router.register('posts', PostViewSet)
api_v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
api_v1_router.register(r'groups', GroupViewSet)
api_v1_router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    # адреса, заданные роутером
    path('', include(api_v1_router.urls)),
    # эндпоинты djoser (user, token, jwt)
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами
    # меняем адрес с auth/jwt/ на jwt/
    path('', include('djoser.urls.jwt')),
]
