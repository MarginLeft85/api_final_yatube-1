from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination

from .permissions import AuthorOrReadOnly
from .serializers import CommentSerializer, FollowSerializer, \
    GroupSerializer, PostSerializer
from posts.models import Group, Post

User = get_user_model()


class GetPostViewSet(
        CreateModelMixin, ListModelMixin, viewsets.GenericViewSet):
    """Собираем вьюсет, который работает только с create и retrieve."""
    pass


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для комментов."""
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        """Определяем метод get_queryset, чтобы выполнить фильтрацию объектов
        по значению из url ('post_id' берем из urls.py: <post_id>)"""
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return post.comments

    def perform_create(self, serializer):
        """Изменяем метод create для комментов."""
        # ищем пост по id (post_id берем из url)
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        # добавляем в сериалайзер поля, которых не было в запросе.
        # автора берем из request, post_id - из объекта выше
        serializer.save(
            author_id=self.request.user.id, post_id=post.id)


class FollowViewSet(GetPostViewSet):
    """Вьюсет для подписок. Наследуем от собственного базового класса
    GetPostViewSet. С ограниченным перечнем методов"""
    serializer_class = FollowSerializer
    # добавляем пермишен: только зарегистрированные
    # пользователи могут отправлять запрос
    permission_classes = (permissions.IsAuthenticated,)
    # добавляем поле для поиска по following.username
    filter_backends = (filters.SearchFilter,)
    # данные будут искаться по обоим полям (OR)
    search_fields = ('following__username', 'user__username')

    def get_queryset(self):
        """Определяем метод get_queryset, чтобы выполнить фильтрацию объектов
        queryset по значению из url ('post_id' берем из urls.py: <post_id>)"""
        user = get_object_or_404(User, username=self.request.user.username)
        return user.follower

    def perform_create(self, serializer):
        """Изменяем метод create для подписок."""
        # имя пользователя берем из запроса и подставляем автоматически
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для групп. Наследуем от ReadOnlyModelViewSet"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # устанавливаем класс пагинации
    pagination_class = LimitOffsetPagination
    # устанавливаем пермишены
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        """Изменяем метод create для постов."""
        # автора берем из запроса и подставляем значение автоматически
        serializer.save(author_id=self.request.user.id)
