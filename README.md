# Поиск сов на Devman

Выводит количество пользователей отправивших решение задач в установленные рамки(по умолчанию с 0:00 до 6:00)

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5.
Для установки временных рамок изменяются константы в исходном коде: 

1. `START_NIGHT_HOUR` - начальный час 
2. `STOP_NIGHT_HOUR` - конечный час.

Пример на Linux:

```bash

$ python seek_dev_nighters.py
Всего сов:  8
6006l1k
PeterChe
kosmontin
constantinovich
1d964ba0d0604b37
idmedvedevivan
andreishkilev1993
ekluev

```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)

