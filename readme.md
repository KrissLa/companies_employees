Запуск:

    - sudo docker-compose up -d --build

Запуск тестов:

    - sudo docker-compose exec web pipenv run pytest

Создание суперпользователя:

    - sudo docker-compose exec web pipenv run python manage.py createsuperuser

Линтеры:

    - sudo docker-compose exec web pipenv run black --exclude=migrations .
    - sudo docker-compose exec web pipenv run flake8 .
    - sudo docker-compose exec web pipenv run mypy .
    - sudo docker-compose exec web pipenv run pylint backend config tests