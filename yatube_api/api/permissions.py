from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """Пермишн, позволяющий читать объекты всем пользователям,
    а изменять только авторам."""
    # в этом методе определяем, разрешен ли, в общем, запрос
    # "разрешение на уровне запроса"
    def has_permission(self, request, view):
        # TRUE для безопасных методов или аутентифицированных пользователей
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    # в этом методе определяем, есть ли у пользователя доступ к данным
    # "разрешение на уровне объекта"
    def has_object_permission(self, request, view, obj):
        return (
            # без этой строки не отрабатывает get по конкретному id поста
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
