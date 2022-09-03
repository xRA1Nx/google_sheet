<b>Конфигурация проекта</b><br>
<ul>
<li>БД - postgress</li>
<li>ORM - Django</li>
<li>Таскер - Django-apshedular </li>
<li>bot - pyTelegramBotAPI</li>
<li>источник данных для парсинга (Google Sheets) - https://docs.google.com/spreadsheets/d/1D33t6I_5MeIvB-mhtv6BUjV6Wyhfxc6lufsUx51A1s8/edit#gid=0</li>
</ul>

<b>Настройки:</b><br>
в файл .env необходимо заполнить своими настройками(secret key, token и т.д.) по примеру файла <b>example.txt</b></br>
Также необходимо указать ID канала, куда бот будет отправлять сообщение(пример инструкции как можно узнать ID канала - https://smmx.ru/telegram/how-to-use/kak-uznat-id-kanala.html)</br>

<b>Старт проекта</b>
docker-compose build (создаем/импортируем образы) <br>
<ol>
<li>
Предзапуск (для применения миграций)--<br>
в 1-й консоли:<br>
docker-compose up<br>
во 2-й консоли:<br>
docker-compose run web python manage.py migrate<br>
docker-compose down<br>
 </li>
<li>
Запуск<br>
в 1-й консоли (запуск приложения django):<br>
docker compose up<br>
во 2-й консоли (запускаем non stop parser):<br>
docker compose run web python manage.py runparser<br>
  </li>
</ol>
<b>Краткое описание функционала:</b><br>

<b>Бот:</b> Отправляет уведомление в указанный канал в случае если текущая дата > срока поставки. при этом такому заказу проставляется соответсвующая отметка информирования в БД чтобы исключить повторное оповещение.<br>

<b>Парсинг + googlesheet</b><br>
Обновление БД актуальной информацией(CRUD) из google sheet, парсинг актуального курса валюты из центробанка.
