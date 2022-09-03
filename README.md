<b>Конфигурация проекта</b><br>
<ul>
<li>БД - postgress</li>
<li>ORM - Django</li>
<li>Таскер - Django-apshedular </li>
<li>bot - pyTelegramBotAPI</li>
<li>источник данных для парсинга (Google Sheets) - https://docs.google.com/spreadsheets/d/1D33t6I_5MeIvB-mhtv6BUjV6Wyhfxc6lufsUx51A1s8/edit#gid=0</li>
</ul>

<b>настройки</b>
в файл .env необходимо заполнить своими настройками(secret key, token и т.д.) по примеру файла example.txt</br>
Также необходимо указать ID канала, куда бот будет отправлять сообщение(пример инструкции как можно узнать ID канала - https://smmx.ru/telegram/how-to-use/kak-uznat-id-kanala.html)</br>

<b>Старт проекта</b>
docker-compose build
--предзапуск проекта (для применения миграций)--
в 1-й консоли:
docker-compose up
во 2-й консоли:
docker-compose run web python manage.py migrate
docker-compose down
--ЗАПУСК ПРОЕКТА--
в 1-й консоли (запуск приложения django):
docker compose up
во 2-й консоли (запускаем non stop parser):
docker compose run web python manage.py runparser

<b>Краткое описание функционала:</b><br>

<b>Бот:</b> Отправляет уведомление в указанный канал в случае если текущая дата > срока поставки. при этом такому заказу проставляется соответсвующая отметка информирования в БД чтобы исключить повторное оповещение.<br>

<b>Парсинг + googlesheet</b><br>
Обновление БД актуальной информацией(CRUD) из google sheet, парсинг актуального курса валюты из центробанка.
