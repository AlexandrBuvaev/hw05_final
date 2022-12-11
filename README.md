# Yatube

[![CI](https://github.com/yandex-praktikum/hw05_final/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw05_final/actions/workflows/python-app.yml)

Учебный проект курса python-разработчик от Яндекс.Практикум.
Социальная сеть блогеров, которая позволяет публиковать посты, комментировать их.
Так же пользователи могут подписываться на других авторов.
### Как запустить проект на устройстве:

- Создаем рабочую директорию для проекта:
```bash
mkdir test_directory
cd test_directory
```
- Копируем проект в рабочую директорию:
```bash
~/test_directory$ git clone git@github.com:AlexandrBuvaev/yatube.git
```
- Создаем виртуальное окружение и устанавливаем зависимости:
```bash
~/test_directory$ python3 -m venv venv
~/test_directory$ source venv/bin/activate
~/test_directory$ pip install -r requirements.txt
```
- Устанавливаем миграции и запускаем проект:
```bash
~/test_directory/yatube python3 manage.py migrate
~/test_directory/yatube python3 manage.py runserver
```
