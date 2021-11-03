# import requests
# from decouple import config
# from bs4 import BeautifulSoup
#
# URL ="https://cars.kg/offers/?vendor=57fa24ee2860c45a2a2c0905"
# HEDERS = {
#     "user=agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
#     "accept": "*/*"
# }
#
# def get_html(url, params=None):
#     reg = requests.get(url, headers=HEDERS, params=params)
#     return reg
# def get_content(html):
#     soup = BeautifulSoup(html.text, "html.parser")
#     items = soup.find_all('a', class_="catalog-list-item")
#     cars = []
#     for item in items:
#         cars.append({
#             "name": item.find("span", class_="catalog-item-caption").get_text().replace('\n            ', '')
#         })
#
#     print(cars)
# def parse():
#     html = get_html(URL)
#     if html.status_code == 200:
#         get_content(html)
#         pass
# parse()
