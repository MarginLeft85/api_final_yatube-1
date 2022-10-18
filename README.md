### Описание:

Этот проект позволяет закрепить полученные знания по api на базе Django REST Framework. Никакой практической ценности для стороннего пользователя не несет. Графомания в чистом виде.

### Как запустить проект (Windows):

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/madzone1987/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Некоторые примеры запросов к API:

Получение публикаций (GET):

```
http://127.0.0.1:8000/api/v1/posts/
```

Создание публикации (POST):

```
http://127.0.0.1:8000/api/v1/posts/

{
  "text": "string",
  "image": "string",
  "group": 0
}

```

Работа с конкретной публикацией по id (GET, PUT, PATCH, DELETE):

```
http://127.0.0.1:8000/api/v1/posts/{id}/
```

Работа с комментариями (GET, POST):

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

Работа с конкретным комментарием по id (GET, PUT, PATCH, DELETE):

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

Получить список групп (GET):

```
http://127.0.0.1:8000/api/v1/groups/
```

Получить конкретную группу (GET):

```
http://127.0.0.1:8000/api/v1/groups/{id}/
```

Работа с подписками (GET, POST):

```
http://127.0.0.1:8000/api/v1/follow/
```

Создать токен для пользователя (POST):

```
http://127.0.0.1:8000/api/v1/jwt/create/

{
  "username": "string",
  "password": "string"
}

```

Обновить токен для пользователя (POST):

```
http://127.0.0.1:8000/api/v1/jwt/refresh/

{
  "username": "string",
  "password": "string"
}

```

Проверить токен (POST):

```
http://127.0.0.1:8000/api/v1/jwt/refresh/

{
  "token": "string"
}

```
