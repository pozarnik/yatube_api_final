### Описание:

API для проекта [YaTube](https://github.com/pozarnik/yatube)

## Технологии

- Python 3.9
- Django 3.2
- Django REST framework 3.12.4

### Запуск проекта в dev-режиме

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/pozarnik/yatube_api_final.git
```

```
cd yatube_api_final
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd yatube_api
```

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Документация по API

Запустите сервер и перейдите по адресу:

```
http://127.0.0.1:8000/redoc/
```

## Мои профили

- [GitHub](https://github.com/pozarnik/)
- [LinkedIn](https://www.linkedin.com/in/alekseyevich-ivan/)

## License

MIT
