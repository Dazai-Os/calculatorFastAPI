# FastAPI Calculator
__FastAPI__ __Calculator__ - это приложение калькулятора написанное на языке программирование python с применением фреймворка FastAPI

### Что он умеет:
* Вычислять переданные значения слева направо (/calc)
* Просматривать последние от 0 до 30 записей (/history)

## Содержание:
1. Сборка проекта и локальный запуск
    * Клонируем репозиторий 
    * Настройка
    * Запуск
    * Открываем сайт
 2. Работа с калькулятором
    * Вычисление с одним аргументом
    * Вычисление с двумя аргументами
    * Запрос истории с default limit и заданным значением
3. Мысли по реализации
    * Ошибка с валидацией данных(или почему не выполнено одно требование)
    * Варианты решения
    * Почему asyncpg
    
____
    
## Сборка проекта и локальный запуск:
### Клонируем репозиторий
Выполните в консоли 
    
`git clone https://github.com/Dazai-Os/calculatorFastAPI`
    
    
`pip install -r requirements.txt`
    

### Настройка
Создайте файл .env и добавьте туда следующие параметры
```
DB_USER=имя пользователя базы данных

PG_PASSWORD=postgres пароль

DB_PASS=пароль от базы данных

DB_NAME=имя базы данных

DB_HOST=Хост базы данных
```
### Запуск приложения
В консоле запустите main.py

` python main.py `

### Открываем сайт
Переходим по ссылке http://127.0.0.1:8000/docs

Это авто документация предоставляемая самим FastAPI, что называется из коробки (реализует Swagger UI)

____

## Работа с калькулятором
### Вычисления с 1 аргументом
Открываем Post /calc кнопка Try  it out. В ставшем доступне окне заполняем json данные по примеру

![](https://github.com/Dazai-Os/calculatorFastAPI/blob/master/other(photo)/photo_2022-02-26_18-48-26.jpg)

Ответ от сервера с успешным результатом:

![](https://github.com/Dazai-Os/calculatorFastAPI/blob/master/other(photo)/photo_2022-02-26_19-06-40.jpg)

### Вычисления с 2 аргументами и более
Заполняем json файл по примеру(2 аргумента):

![](https://github.com/Dazai-Os/calculatorFastAPI/blob/master/other(photo)/photo_2022-02-26_20-08-54.jpg)

Полученный ответ от сервера:

![](https://github.com/Dazai-Os/calculatorFastAPI/blob/master/other(photo)/photo_2022-02-26_20-09-10.jpg)

От 2 и более аргументов

![](https://github.com/Dazai-Os/calculatorFastAPI/blob/master/other(photo)/photo_2022-02-26_20-21-31.jpg)

Полученный ответ от сервера:

![](https://github.com/Dazai-Os/calculatorFastAPI/blob/master/other(photo)/photo_2022-02-26_20-21-36.jpg)

Как можно было понять, чтобы добавить аргументы, мы их перечисляем через запятую в списке по примеру 2 аргумента

### Запрос истории с default и заданным  значением
Открываем Post /history нажимаем Try it out. В ставшем доступном окне заполняем json файл

С заданными параметрами:

![](https://github.com/Dazai-Os/calculatorFastAPI/blob/master/other(photo)/photo_2022-02-26_20-27-02.jpg)

Ответ сервера:

![](https://github.com/Dazai-Os/calculatorFastAPI/blob/master/other(photo)/photo_2022-02-26_20-27-07.jpg)

Значение по умолчанию 30, можно или вообше не изменять или передавать пустой json файл, как в примере:

![](https://github.com/Dazai-Os/calculatorFastAPI/blob/master/other(photo)/photo_2022-02-26_20-31-24.jpg)

Ответ сервера(Сервер вернул только 6 значений, из-за того что в базе данных их всего 6):

![](https://github.com/Dazai-Os/calculatorFastAPI/blob/master/other(photo)/photo_2022-02-26_20-31-28.jpg)
