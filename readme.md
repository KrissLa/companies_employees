Запуск:

    - sudo docker-compose up -d --build

Запуск тестов:

    - sudo docker-compose exec web pipenv run pytest

Создание суперпользователя:

    - sudo docker-compose exec web pipenv run python manage.py createsuperuser