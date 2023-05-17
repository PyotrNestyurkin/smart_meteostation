# import requests
# from bs4 import BeautifulSoup
#
# HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}
#
#
# def get_html(url):
#     return requests.get(url, headers=HEADERS)
#
#
# def get_contect(html):
#     soup = BeautifulSoup(html.text, 'html.parser')
#     items = soup.find('span', class_='goroda')
#     soup_2 = BeautifulSoup(str(items), 'html.parser')
#     days_info = list(soup_2.find_all('a'))
#     regions = [day.get("href") for day in days_info]
#     print(regions)
#     # formatted_days = ''.join(str(i) for i in days_info)
#     # soup_3 = BeautifulSoup(formatted_days, 'html.parser')
#     # forecast_days = list(soup_3.find_all('href', class_='tridenb'))
#
#
# def get_info(url):
#     url = 'http://kalendar-rybolova.ru/'
#     html = get_html(url)
#     return get_contect(html)
#
#
# get_info('http://kalendar-rybolova.ru/')

regions = ['/kirovskaya-oblast/', '/kostromskaya-oblast/', '/krasnoyarskij-kraj/', '/kurganskaya-oblast/',
           '/kurskaya-oblast/', '/lipeckaya-oblast/', '/magadanskaya-oblast/', '/murmanskaya-oblast/',
           '/nizhegorodskaya-oblast/', '/novgorodskaya-oblast/', '/novosibirskaya-oblast/', '/omskaya-oblast/',
           '/orenburgskaya-oblast/', '/orlovskaya-oblast/', '/penzenskaya-oblast/', '/permskij-kraj/',
           '/primorskij-kraj/', '/pskovskaya-oblast/', '/respublika-adygeya/', '/respublika-altaj/',
           '/respublika-bashkortostan/', '/respublika-buryatiya/', '/respublika-dagestan/', '/respublika-ingushetiya/',
           '/respublika-kabardino-balkariya/', '/respublika-kalmykiya/', '/respublika-karachaevo-cherkessiya/',
           '/respublika-kareliya/', '/respublika-komi/', '/respublika-krym/', '/respublika-marij-ehl/',
           '/respublika-mordoviya/', '/respublika-saha-(yakutiya)/', '/respublika-severnaya-osetiya-alaniya/',
           '/respublika-tatarstan/', '/respublika-tyva/', '/respublika-udmurtiya/', '/respublika-hakasiya/',
           '/ryazanskaya-oblast/', '/samarskaya-oblast/', '/saratovskaya-oblast/', '/sahalinskaya-oblast/',
           '/smolenskaya-oblast/', '/stavropolskij-kraj/', '/tambovskaya-oblast/', '/tverskaya-oblast/',
           '/tomskaya-oblast/', '/tulskaya-oblast/', '/tyumenskaya-oblast/', '/ulyanovskaya-oblast/',
           '/habarovskij-kraj/', '/hanty-mansijskij-ao-yugra/', '/chelyabinskaya-oblast/', '/chechenskaya-respublika/',
           '/chuvashskaya-respublika/', '/yamalo-neneckij-ao/', '/yaroslavskaya-oblast/']

region_sl = {'50': '/moskovskaya-oblast/', '90': '/moskovskaya-oblast/', '99': '/moskovskaya-oblast/',
             '47': '/leningradskaya-oblast/', '98': '/leningradskaya-oblast/', '23': '/krasnodarskij-kraj/',
             '93': '/krasnodarskij-kraj/', '66': '/sverdlovskaya-oblast/', '96': '/sverdlovskaya-oblast/',
             '61': '/rostovskaya-oblast/', '22': '/altajskij-kraj/', '28': '/amurskaya-oblast/',
             '29': '/arhangelskaya-oblast/', '30': '/astrahanskaya-oblast/', '31': '/belgorodskaya-oblast/',
             '33': '/vladimirskaya-oblast/', '34': '/volgogradskaya-oblast/', '35': '/vologodskaya-oblast/',
             '36': '/voronezhskaya-oblast/', '79': '/evrejskaya-avtonomnaya-oblast/', '75': '/zabajkalskij-kraj/',
             '80': '/zabajkalskij-kraj/', '37': '/ivanovskaya-oblast/', '38': '/irkutskaya-oblast/',
             '39': '/kaliningradskaya-oblast/',
             '40': '/kaluzhskaya-oblast/', '41': '/kamchatskij-kraj/', '42': '/kemerovskaya-oblast/',
             }