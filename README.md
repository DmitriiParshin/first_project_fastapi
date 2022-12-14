# Python application with FastApi and Docker
### Технологии
- Python 3.10.7
- FastApi 0.88.0
- SQLAlchemy 1.4.45
- Docker 20.10.16
- docker-compose 1.29.2
### Как запустить приложение, используя Docker:

Клонировать репозиторий:

```
git clone https://github.com/DmitriiParshin/first_project_fastapi.git
```

В директории проекта создать файл .env, в котором прописать переменные окружения:

- DB_NAME=fastapi_app.db
- SECRET_KEY=secret

Запустить приложение в контейнере:

```
docker-compose up
```

Документация для приложения:

```
http://127.0.0.1:8000/docs/
```

### Как запустить проект без использования Docker:

Клонировать репозиторий:

```
git clone https://github.com/DmitriiParshin/first_project_fastapi.git
```

Перейти в директорию проекта:

```
cd first_project_fastapi
```

Cоздать виртуальное окружение:

```
python3 -m venv env
```

Активировать виртуальное окружение:

```
source venv/bin/activate
```

Установить зависимости:

```
pip install -e .
```

Запустить приложение:

```
uvicorn main:app
```

Документация для приложения:

```
http://127.0.0.1:8000/docs/
```

### Автор
Dmitry Parshin