import datetime as dtime
from django.core.exceptions import ValidationError
from parsers.sheet_pars import get_sheet_data
from App.models import GoogleSheet
# from telbot.botapp import bot_inform

def checker() -> None:
    flag_need_inform = False  # флаг определяющий нужно ли Боту отправлять уведомление
    message_inform = ""

    today = dtime.date.today()
    sheet_data = get_sheet_data()
    db_data = GoogleSheet.objects.all()  # получаем данные БД

    for key, val in sheet_data.items():
        try:
            qs = db_data.filter(order=key)
            if not qs.exists():
                # смотрим существует ли в БД такой обьект и если его нет то создаем
                GoogleSheet.objects.create(
                    order=key,
                    rub_price=val["стоимость, руб."],
                    usd_price=val["стоимость, $"],
                    delivery_time=val["срок поставки"], )
            else:
                obj = qs[0]
                # если данные не совпадают то обновляем их и сбрасываем notify на начальное значение
                if obj.usd_price != val["стоимость, $"]:
                    qs.update(usd_price=val["стоимость, $"],
                              notify=False)
                if obj.delivery_time != val["срок поставки"]:
                    qs.update(delivery_time=val["срок поставки"],
                              notify=False)
        except ValidationError as v:
            print(f"Ошибка: {v}")
        except ValueError as val_e:
            print(f"Ошибка: {val_e}")

    for obj in db_data:
        # если в БД есть заказ которого нет в парсере, удаляем его из БД
        if str(obj.order) not in sheet_data:
            obj.delete()

        """Если срок поставки больше текущей даты и 
        и бот по этому заказу ранее не информировал"""
        if today > obj.delivery_time and not obj.notify:
            message_inform += f"заказ№ {obj.order} просрочен\n"
            flag_need_inform = True
            obj.notify = True  # изменяем поле уведомления в заказе
            obj.save()

    # if flag_need_inform:  # если есть заказы по которым нужно уведомить
    #     bot_inform(message_inform)
    flag_need_inform = False  # возвращаем флаг в default
