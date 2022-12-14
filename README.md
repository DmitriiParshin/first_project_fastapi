# Python application with FastApi and Docker
### Технологии
- Python 3.10.7
- FastApi 0.88.0
- SQLAlchemy 1.4.45
- Docker 20.10.16
- docker-compose 1.29.2
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/DmitriiParshin/first_project_fastapi.git
```

```
cd first_project_fastapi
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости:

```
pip install -e .
```

Запустить приложение:

```
uvicorn main:app
```

Запустить приложение в контейнере:

```
docker-compose up
```

Документация для приложения:

```
http://127.0.0.1:8000/docs/
```

### Автор
Dmitry Parshin