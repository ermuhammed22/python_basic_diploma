### Описание проекта
Целью создания telegram-бота является предоставление пользователям 
удобного инструмента для получения информации о различных параметрах
товаров или услуг через интеграцию с API стороннего сайта. Бот 
позволяет быстро получить минимальные, максимальные или произвольные
значения по заданным критериям, что упрощает процесс поиска и 
сравнения необходимой информации.

### Как пользоваться

#### custom command:

**/low** - выводит минимальные значения, такие как самая низкая стоимость товара/услуги.

Запрос без параметров:

CURL GET https://yandex.ru/dev/dictionary

Пример ответа запроса:

```console
{
    "data": [
        {
            "depart_date": "2024-04-04",
            "origin": "MOW",
            "destination": "HKT",
            "gate": "Biletix",
            "return_date": "2024-04-08",
            "found_at": "2024-03-22T18:43:12Z",
            "trip_class": 0,
            "value": 67810,
            "number_of_changes": 2,
            "duration": 5585,
            "distance": 7479,
            "show_to_affiliates": true,
            "actual": true
        },
        {
            "depart_date": "2024-04-03",
            "origin": "MOW",
            "destination": "HKT",
            "gate": "Kupi.com",
            "return_date": "2024-04-07",
            "found_at": "2024-03-24T11:16:30Z",
            "trip_class": 0,
            "value": 73340,
            "number_of_changes": 3,
            "duration": 2840,
            "distance": 7479,
            "show_to_affiliates": true,
            "actual": true
        }
    ]
}
```

**/high** - выводит максимальные значения, например, самая высокая стоимость товара/услуги.

Запрос без параметров:

CURL GET https://yandex.ru/dev/dictionary

Пример ответа запроса:

```console
{
    "data": [
        {
            "depart_date": "2024-04-05",
            "origin": "MOW",
            "destination": "HKT",
            "gate": "Expedia",
            "return_date": "2024-04-10",
            "found_at": "2024-03-20T22:41:35Z",
            "trip_class": 0,
            "value": 79860,
            "number_of_changes": 2,
            "duration": 8430,
            "distance": 7479,
            "show_to_affiliates": true,
            "actual": true
        },
        {
            "depart_date": "2024-04-07",
            "origin": "MOW",
            "destination": "HKT",
            "gate": "Aviasales",
            "return_date": "2024-04-11",
            "found_at": "2024-03-26T10:35:49Z",
            "trip_class": 0,
            "value": 81130,
            "number_of_changes": 3,
            "duration": 1790,
            "distance": 7479,
            "show_to_affiliates": true,
            "actual": true
        }
    ]
}
```

**/custom** - выводит произвольные значения по заданным параметрам.

Запрос с параметрами:
CURL POST https://yandex.ru/dev/dictionary

Пример ответа запроса:

```console
{
    "data": [
        {
            "id": 1,
            "name": "Product 1",
            "price": 10
        },
        {
            "id": 2,
            "name": "Product 2",
            "price": 9
        },
        ...
        {
            "id": 10,
            "name": "Product 10",
            "price": 1
        }
    ]
}
```

Для запроса с параметрами используем всегда POST запрос к API


#### default command:

**/start** - старт, инициализация бота.

**/help** - помощь, получение помощи и описания команд.

### Как запустить
Для запуска проекта на стороннем ПК необходимо выполнить 
следующие шаги:

1. Склонировать репозиторий с проектом.
2. Установить необходимые библиотеки с помощью команды 
pip install -r requirements.txt. 
3. Запустить скрипт main.py. 
4. Взаимодействовать с ботом через Telegram, используя 
предоставленные команды.

Эти шаги можно выполнить с помощью следующих команд:

```Terminal
git clone https://github.com/your-repo/project.git
cd project
pip install -r requirements.txt
python main.py
```

После запуска проекта в Telegram можно начать использовать бота, выполняя указанные команды.