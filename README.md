# Yacut

## Описание

Учебный проект для практики работы во фреймворке Flask.

**Yacut** - это сервис укорачивания ссылок, который ассоциирует длинную пользовательскую ссылку с короткой. Короткую ссылку может предложить сам пользователь, или же сервис самостоятельно её сгенерирует.

Иными словами, при помощи данного сервиса пользователь может превратить длинную и неудобную ссылку наподобие "https://flask.palletsprojects.com/en/2.2.x/changes/#version-2-0-0" в короткую - "http://localhost/ver2". После создания короткой ссылки при переходе по ней происходит переадресация на исходный адрес.

Помимо работы в браузере с графическим интерфейсом всем желающим доступен API, дублирующий весь функционал сервиса.

## Ключевые технологии и библиотеки:
- [Python](https://www.python.org/);
- [Flask](https://pypi.org/project/Flask/);
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/);

## Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Gavral/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создайте в корневой директории файл .env со следующим наполнением:

```
FLASK_APP=yacut
FLASK_ENV=development или production
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=<ваш_секретный_ключ>
```

## Управление:

Для локального запуска выполните команду:

```
flask run
```

Сервис будет запущен и доступен по следующим адресам:

- http://localhost/ - главная страница сервиса;

- http://localhost/api/id/ - эндпоинт, принимающий POST-запросы;

    * Схема POST-запроса:
        ```json
        {
        "url": "string",
        "custom_id": "string"
        }
        ```

    * Схема ответа на POST-запрос:
        ```json
        {
        "url": "string",
        "short_link": "string"
        }
        ```

- http://localhost/api/id/<short_id>/ - эндпоинт, принимающий GET-запросы.
    
    В адресе вместо <short_id> должна быть указана введённая или сгенерированная короткая ссылка.

    * Схема ответа на GET-запрос:
        ```json
        {
        "url": "string"
        }
        ```

    Полная спецификация API доступна в репозитории - файл openapi.yml

### Автор

Гаврилов Александр

gavrilov-al@mail.ru
