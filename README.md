### Описание проекта
Целью создания telegram-бота является предоставление пользователям
удобного инструмента для получения информации о погоде в различных
городах. Бот использует API OpenWeatherMap для получения данных о
текущей погоде, а также предоставляет функционал истории запросов
пользователей.

### Как пользоваться

#### custom command:

**/low** - выводит минимальные значения температуры в указанном 
городе.

Пример использования:

```bash
/low
```

Пример ответа запроса:

```console
Минимальная температура в городе Moscow сегодня: -3°C"
```

**/high** - выводит максимальные значения температуры в указанном 
городе.

Пример использования:

```bash
/high
```

Пример ответа запроса:

```console
Максимальная температура в городе Moscow сегодня: 8°C"
```

**/custom** - выводит полную информацию о погоде в указанном городе.

Пример использования:

```bash
/custom
```

Пример ответа запроса:

```console
Погода в городе Moscow сегодня:
Описание: облачно
Температура сейчас: 2°C (Ощущается как -1°C)
Минимальная температура: -3°C
Максимальная температура: 8°C
Влажность: 86%
Скорость ветра: 4.12 м/с
```

**/history ** - показывает последние 10 запросов пользователя.

Пример использования:

```bash
/history
```

Пример ответа запроса:

```console
История ваших запросов:
1. Команда: /custom, Аргументы: Moscow
2. Команда: /high, Аргументы: Moscow
```

#### default command:

**/start** - старт, инициализация бота.

**/help** - помощь, получение помощи и описания команд.

### Как запустить
Для запуска проекта на стороннем ПК необходимо выполнить 
следующие шаги:

1. Склонировать репозиторий с проектом.
2. Создайте файл .env на основе .env.template и заполните 
необходимые переменные.
3. Установить необходимые библиотеки с помощью команды 
pip install -r requirements.txt. 
3. Запустить скрипт main.py. 
4. Взаимодействовать с ботом через Telegram, используя 
предоставленные команды.

Эти шаги можно выполнить с помощью следующих команд:

```Terminal
git clone https://gitlab.skillbox.ru/ermukhammed_kasymbekov/python_basic_diploma
cd project
cp .env.template .env
nano .env  # заполните необходимые переменные
pip install -r requirements.txt
python main.py
```

### Структура проекта

project/
│
├── api/
│   └── api.py
│
├── config_data/
│   ├── __init__.py
│   └── config.py
│
├── database/
│   └── database.py
│
├── handlers/
│   ├── __init__.py
│   ├── default_handlers/
│   │   ├── __init__.py
│   │   ├── custom.py
│   │   ├── echo.py
│   │   ├── help.py
│   │   ├── high.py
│   │   ├── history.py
│   │   └── low.py
│   └── custom_handlers/
│       └── (other custom handlers)
│
├── keyboards/
│   ├── __init__.py
│   ├── reply.py
│   └── inline.py
│
├── utils/
│   ├── __init__.py
│   ├── misc.py
│   └── set_bot_commands.py
│
├── loader.py
├── main.py
├── .env
├── .env.template
└── requirements.txt

### Функции работы с базой данных

Модуль database/database.py содержит функции для работы с базой данных:

    create_history_table() - Создание таблицы истории запросов.
    insert_user_history(user_id, command, arguments) - Вставка новой записи в таблицу истории.
    get_user_history(user_id) - Получение истории запросов пользователя.
    log_command(user_id, command, arguments=None) - Запись команды в историю.

Пример использования:

from database.database import create_history_table, log_command, get_user_history

# Создание таблицы истории
create_history_table()

# Запись команды в историю
log_command(user_id=123, command='/custom', arguments='Moscow')

# Получение истории запросов
history = get_user_history(user_id=123)
print(history)


После запуска проекта в Telegram можно начать использовать бота, 
выполняя указанные команды.