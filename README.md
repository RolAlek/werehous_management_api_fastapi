# werehous_management_api_fastapi

Небольшой API-клиент для управления складом. Крутится в докер-контейнерах, что позволяет развернуть приложение в одну команду.

## Стек:
* Python 3.12,
* Fastapi 0.112.2,
* SQLAlchemy 2.0.32
* PostgreSQL + asyncpg
* Alembic 1.13.2
* Docker и Docker-compose

## Установка и настройка:
* Клоинрутйе репозиторий;
* В корне проекта создайте `.env` файл и заполните его в соответсвии с `.env.example`:
```
POSTGRES_USER=ваше пользователь от ДБ
POSTGRES_PASSWORD=ваш пароль от ДБ
POSTGRES_DB=notes

APP__DB__URL=postgresql+asyncpg://pg_user:pg_password@db:5432/notes
APP__DB__ECHO=0
```
### Docker:
В корне проекта выполните команду:

```sh
docker compose up
```

Перейдите по адресу `http://0.0.0.0:8000/docs` и... И все - радуйтесь!

### Для разработки:
Установите менеджер зависимостей poetry:
```sh
pip install poetry
```
Установите зависимости:
```sh
poetry install
```
Активируйте виртуальное окружение:
```sh
poetry shell
```
Запустите приложение и перейдите по адресу `http://127.0.0.1:8000/docs` для ознакомления с документацией к API и тестирования эндпоинтов.
```sh
uvicorn main:main_app
```