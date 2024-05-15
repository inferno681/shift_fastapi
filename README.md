<div id="header" align="center">
  <img src="https://img.shields.io/badge/Python-3.12.3-F8F8FF?style=for-the-badge&logo=python&logoColor=20B2AA">
  <img src="https://img.shields.io/badge/FastAPI-0.111.0-F8F8FF?style=for-the-badge&logo=FastAPI&logoColor=20B2AA">
  <img src="https://img.shields.io/badge/PostgreSQL-555555?style=for-the-badge&logo=postgresql&logoColor=F5F5DC">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0.30-F8F8FF?style=for-the-badge&logo=SQLAlchemy&logoColor=20B2AA">
  <img src="https://img.shields.io/badge/Pydantic-2.7.1-F8F8FF?style=for-the-badge&logo=pydantic&logoColor=20B2AA">
  <img src="https://img.shields.io/badge/Uvicorn-0.29.0-F8F8FF?style=for-the-badge&logo=uvicorn&logoColor=20B2AA">
  <img src="https://img.shields.io/badge/Alembic-1.13.1-F8F8FF?style=for-the-badge&logo=alembic&logoColor=20B2AA">
  <img src="https://img.shields.io/badge/Docker-555555?style=for-the-badge&logo=docker&logoColor=2496ED">
</div>

<br>

Документация к API будет доступна по url-адресу [shift-fastapi/SWAGER](http://shift-fastapi.ddns.net/docs)


<details><summary><h1>Тестовое задание SHIFT на курс «Python»</h1></summary>

* **Задача:**
  + Реализация REST-сервис просмотра текущей зарплаты и даты следующего повышения.

* **Особенности:**
  + Сервис реализован на FastAPI.
  + Зависимости зафиксированы менеджером зависимостей poetry.
  + Написаны тесты с использованием pytest.
  + Реализована возможность собирать и запускать контейнер с сервисом в Docker.


</details>

<details><summary><h1>Инструкция по установке</h1></summary>

Клонируйте репозиторий и перейдите в него.
```bash
git@github.com:inferno681/shift_fastapi.git
```

Для установки виртуального окружения с помощью **Poetry** нужно установить его через pip:
```bash
pip install poetry
```
Для активации poetry нужно прописать:
```bash
poetry install
```

### Работа с зависимостями
Обновления зависимостей (при загрузки обновлений репозитория с GitHub):
```bash
poetry update
```
Создайте файл **.env**, в корневой папке проекта, с переменными окружения.

  ```
  APP_TITLE = Shift FastAPI
  APP_DESCRIPTION = Salary view service
  SECRET = Secret
  DB_HOST = localhost
  DB_PORT = 5432
  DB_USERNAME = user
  DB_PASSWORD = secret_password
  DB_NAME = postgres
  REGISTRATION_ROUTER=True
  USERS_ROUTER=True
  ```


Находясь в корневой папке проекта примените миграции.
  ```
  alembic upgrade head
  ```

Для запуска сервера используйте данную команду:
  ```
  uvicorn app.main:app --reload
  ```

</details>

<details><summary><h1>Запуск проекта через докер</h1></summary>

- Клонируйте репозиторий.
- Перейдите в папку **infra** и создайте в ней файл **.env** с переменными окружения:
    ```
  APP_TITLE = Shift FastAPI
  APP_DESCRIPTION = Salary view service
  SECRET = Secret
  DB_HOST = localhost
  DB_PORT = 5432
  DB_USERNAME = user
  DB_PASSWORD = secret_password
  DB_NAME = postgres
  REGISTRATION_ROUTER=True
  USERS_ROUTER=True
    ```
- Из папки **infra** запустите docker-compose-prod.yaml:
  ```
  ~$ docker compose -f docker-compose-prod.yaml up -d
  ```
- В контейнере **backend** примените миграции:
  ```
  ~$ docker compose -f docker-compose-prod.yaml exec backend alembic upgrade head
  ```

Документация к API будет доступна по url-адресу [127.0.0.1/redoc](http://127.0.0.1/redoc)

</details>

<details><summary>Ссылки на используемые библиотеки</summary>

- [Python](https://www.python.org/downloads/release/python-3123/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Uvicorn](https://www.uvicorn.org/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [Docker](https://www.docker.com/)

</details>

* **Разработчики Backend:**
  + [Василий](https://github.com/inferno681)
