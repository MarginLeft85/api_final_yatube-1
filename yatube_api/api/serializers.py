from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post


User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментов."""
    # переопределяем связанное(related) поле author
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'created', 'post')


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для подписок."""
    # переопределяем связанное(related) поле author
    user = serializers.SlugRelatedField(
        # это поле менять по значению из запроса не будем
        read_only=True,
        slug_field='username',
        # задаем значение по умолчанию, чтобы прошла валидация,
        # так как сущности user еще нет
        # (в perform_create user создается перед записью в БД)
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),    # не понимаю
        slug_field='username')

    class Meta:
        model = Follow
        fields = ('user', 'following')
        # добавляем проверку на уникальность сочетания 2 полей
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Эта подписка уже есть'
            )
        ]

    def validate(self, data):
        """Проверка, чтобы нельзя было подписаться на самого себя"""
        if data['following'] == self.context.get('request').user:
            raise serializers.ValidationError('нельзя подписаться на себя!')
        return data
        # как правильно загуглить, что user в self.context.get('request').user?


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для групп."""

    class Meta:
        # "fields = '__all__'" не используем
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для постов."""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')
