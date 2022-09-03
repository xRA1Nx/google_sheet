import requests
from bs4 import BeautifulSoup


def get_usd():
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').content
    soup = BeautifulSoup(r, 'xml')
    usd = soup.find(ID="R01235")
    return float(usd.Value.getText().replace(',', '.'))


if __name__ == "__main__":
    print(get_usd())
