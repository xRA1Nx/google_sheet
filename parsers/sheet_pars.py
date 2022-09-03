import os.path
import datetime
from googleapiclient.discovery import build
from google.oauth2 import service_account
from parsers.usd_pars import get_usd

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']  # допустимые ресурсы
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRED_PATH = os.path.join(BASE_DIR, 'credentials.json')  # путь к файлу с полномочиями
SHEET_ID = '1D33t6I_5MeIvB-mhtv6BUjV6Wyhfxc6lufsUx51A1s8'  # таблица
SHEET_RANGE = 'Лист1!A1:D'  # диапозон


def get_sheet_data():
    creds = service_account.Credentials.from_service_account_file(CRED_PATH, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_ID, range=SHEET_RANGE).execute()
    db_dict = {}
    usd = get_usd()

    data_from_sheet = result.get('values', [])
    for row in data_from_sheet[1:]:
        if row == [] or "" in row[1:] or len(row[1:]) != 3:  # пропускаем строчки с пустыми значениями
            continue
        try:
            temp_date = row[3].replace('-', '.').replace('/', '.')
            date = datetime.datetime.strptime(temp_date, '%d.%m.%Y').date()
            int(row[2])

        except ValueError as v:
            print(f"Ошибка: {v}")
        except IndexError as ind:
            print(f"Ошибка: {ind}", )
        else:

            db_dict[row[1]] = {
                "стоимость, $": int(row[2]),
                "стоимость, руб.": round(int(row[2]) * usd),
                # "срок поставки": "-".join(row[3].split(".")[::-1]),
                "срок поставки": date
            }

    return db_dict


#
#
# if __name__ == '__main__':
#     get_sheet_data()

if __name__ == "__main__":
    # get_sheet_data()
    print(get_sheet_data())
