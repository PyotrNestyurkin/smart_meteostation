import requests
from bs4 import BeautifulSoup

HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}


def get_html(url):
    return requests.get(url, headers=HEADERS)


def get_contect(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find('div', id='shapka6')
    soup_2 = BeautifulSoup(str(items), 'html.parser')
    days_info = list(soup_2.find_all('tr'))
    formatted_days = ''.join(str(i) for i in days_info)
    soup_3 = BeautifulSoup(formatted_days, 'html.parser')
    forecast_days = list(soup_3.find_all('font', class_='tridenb'))
    forecast_days.extend(soup_3.find_all('font', class_='tridenv'))
    forecast_text = list(soup_3.find_all('td', class_='tridna'))
    return {
        forecast_days[i].get_text(): forecast_text[i].get_text()
        for i in range(3)
    }


def get_info(url):
    html = get_html(url)
    return get_contect(html)


def get_goroda(url):
    html = get_html(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find('span', class_='goroda')
    soup_2 = BeautifulSoup(str(items), 'html.parser')
    days_info = list(soup_2.find_all('a'))
    return [day.get("href") for day in days_info]


