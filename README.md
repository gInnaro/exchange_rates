# exchange_rates
Тестовое задание

Написать сервис "Конвертер валют" который работает по REST-API.
Пример запроса:
GET /api/rates?from=USD&to=RUB&value=1
Ответ:
{
"result": 62.16
}

Задание было реализованно на FastAPI с использование парсинга данных API ЦБ РФ "https://www.cbr-xml-daily.ru/latest.js"
Сервис может посчитать по курсу к рублю, такую валюту как:
"AUD", "AZN", "GBP", "AMD", "BYN", "BGN", "BRL", "HUF", "VND", "HKD", "GEL", "DKK", "AED", "USD", "EUR", "EGP", "INR", "IDR", "KZT", "CAD", "QAR", "KGS", "CNY", "MDL", "NZD", "NOK", "PLN", "RON", "XDR", "SGD", "TJS", "THB", "TRY", "TMT", "UZS", "UAH", "CZK", "SEK", "CHF", "RSD", "ZAR", "KRW", "JPY"
И аналогично обратно к этим валютам
При переходе /docs можно прочитать документацию

Установка Fast API и Requests

pip install fastapi uvicorn, requests

Скачиваем exchange_rates.py

Потом в консоле пишем

uvicorn exchange_rates:app --reload

И в браузере открываем 

http://127.0.0.1:8000/api/rates?froms=USD&to=RUB&value=1
