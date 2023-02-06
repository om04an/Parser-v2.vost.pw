import requests
from bs4 import BeautifulSoup
import time


start_time = time.time()


def parsing_all_pages(page_number):
    url = f'https://v2.vost.pw/page/{page_number}/'
    response = requests.get(url)

    if response.status_code != 200:
        print('Stop, cause: 404')
        return 404

    text_page = response.text
    soup = BeautifulSoup(text_page, 'html.parser')
    all_anime_on_page = soup.find_all('div', 'shortstory')

    for anime in all_anime_on_page:
        name = anime.find('h2').text.split(' / ')[0]
        date = anime.find('span', class_='staticInfoLeftData').text
        link = anime.find('a')['href']
        to_csv(name, date, link)

    parsing_all_pages(page_number + 1)


def to_csv(name, date, link):
    with open('anime_list.csv', 'a') as f:
        f.write(f'{name}, {date}, {link}')


parsing_all_pages(1)

time_spent = time.time() - start_time
print(time_spent, "second")
