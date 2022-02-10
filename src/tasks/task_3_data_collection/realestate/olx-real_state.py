import os
from click import option
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import csv
import time
from tqdm import tqdm
import dateparser
import requests
import enum

from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument("--headless")


class Ad:
    ''''
    The Ad Class represents an ad on the olx website
    '''

    def __init__(self, id: str):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }

        page_src = requests.get(self.get_ad_url(id), headers=headers).content
        soup = BeautifulSoup(page_src, 'lxml')
        self.id = id
        self.soup = soup
        self.price = self.get_price()
        self.title = self.get_title()
        self.location = self.get_location()
        self.date = self.get_date()
        self.description = self.get_description()
        self.views = self.get_views()
        self.owner_name = self.get_owner_name()
        self.owner_id = self.get_owner_id()
        self.fields = {}

        tags = soup.find_all('td', {'class': 'col'})

        for tag in tags:
            field = tag.find('th').text.strip()
            field = ''.join(filter(str.isascii, field))
            field = field.lower().replace(' ', '_')
            field = ''.join(filter(lambda x: x.isalpha() or x == '_', field))
            field_value = tag.find('td').text.strip().replace(
                '\t', '').replace('\n', '')
            self.fields[field] = field_value

        # create variables for each field
        for field, value in self.fields.items():
            setattr(self, field, value)

    @staticmethod
    def get_ad_url(ad: str) -> str:
        return f'https://www.olx.com.eg/en/ad{ad}'

    def __str__(self) -> str:
        return f'{self.title} - {self.price} - {self.location} - {self.date} - {self.fields}'

    def __repr__(self) -> str:
        return f'{self.title} - {self.price} - {self.location} - {self.date} - {self.fields}'

    def get_price(self) -> int:
        price = self.soup.find(
            'div', {'class': 'pricelabel tcenter'})
        if price is None:
            return np.nan
        price = ''.join(filter(str.isdigit, price.text.strip()))
        return int(price)

    def get_title(self) -> str:
        return self.soup.find('h1', {'class': 'brkword lheight28'}).text.strip()

    def get_location(self) -> str:
        return self.soup.find('strong', {'class': 'c2b small'}).text.strip()

    def get_date(self) -> str:
        date = self.soup.find(
            'span', {'class': 'pdingleft10 brlefte5'}).text.strip()
        date = date.split(' Ad ID:')[0]
        date = date.split('Added					at')[1]
        return dateparser.parse(date).strftime('%d/%m/%Y')

    def get_description(self) -> str:
        description = self.soup.find(
            "div", {"id": "textContent", 'class': 'clr'})
        try:
            description = description.text.strip()
        except:
            description = ' '
        return description

    def get_views(self) -> int:
        views = self.soup.find_all(
            'div', {'class': 'pdingtop10'})[-1].text.strip()
        return int(''.join(filter(str.isdigit, views)))

    def get_owner_name(self) -> str:
        owner_name = self.soup.find('p', {'class': 'user-box__info__name'})
        if owner_name is None:
            return 'unknown'
        return owner_name.text.strip()

    def get_owner_id(self) -> str:
        owner_id = self.soup.find('a', {'class': 'user-box__links__link'})
        if owner_id is None:
            return np.nan
        return owner_id['href']


class State(enum.Enum):
    SLOW = 4
    MEDIUM = 2
    FAST = 0.5


class OlxScraper:

    def __init__(self, section: str, range: tuple, interval: int, speed: State = State.MEDIUM) -> None:
        self.section = section
        self.range = range
        self.interval = interval
        self.driver = webdriver.Chrome(options=option)
        self.speed = speed
        self.ranges = self.slice_ranges()
        try:
            os.makedirs('data')
        except FileExistsError:
            print('data folder already exists')

        for start, end in self.ranges:
            if os.path.exists(f'data{os.sep}{self.section}_{start}_{end}.csv'):
                print(f'{self.section}_{start}_{end}.csv already exists')
                continue
            print(f'Scraping {self.section}_{start}_{end}')
            df = self.run(start, end)
            df.to_csv(
                f'data{os.sep}{self.section}_{start}_{end}.csv', index=False)
            print(f'wrote to csv: {self.section}_{start}_{end}.csv')

    def slice_ranges(self) -> list[tuple]:
        return [
            (i, min(i + self.interval, self.range[1]) )
            for i in range(self.range[0], self.range[1], self.interval)
        ]

    def scroll_and_wait(self, sec: float) -> None:
        '''scroll and wait for page to load'''
        sec *= self.speed.value
        time.sleep(sec)
        # scroll to bottom
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight/3);")

        time.sleep(sec / 2)

        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight/1.5);")
        time.sleep(sec / 2)

        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sec)

    def get_num_of_pages(self, soup: BeautifulSoup) -> int:
        '''
        get the number of pages for this section
        '''
        self.scroll_and_wait(3)
        pages_div = soup.find_all("a",
                                  {"class": "block br3 brc8 large tdnone lheight24"})
        try:
            num_of_pages = int(pages_div[-1].text.strip())
        except:
            num_of_pages = 1
        return num_of_pages

    def get_page_link(self, link: str, num: int) -> str:
        '''
        get the link to the page
        '''
        return link + "&page=" + str(num)

    def get_links(self, start_price: int, end_price: int) -> list[str]:
        ''' scrape links for specific price range '''
        ids = []
        link = rf'https://www.olx.com.eg/en/properties/{self.section}/?search%5Bfilter_float_price%3Afrom%5D={start_price}&search%5Bfilter_float_price%3Ato%5D={end_price}'

        self.driver.get(link)
        self.scroll_and_wait(0.5)

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        num_of_pages = self.get_num_of_pages(soup)

        if num_of_pages == 500:
            print(f'{self.section} has more than 500 pages')
            print('Use smaller range')
            return None

        for page in tqdm(range(1, num_of_pages + 1)):
            page_link = self.get_page_link(link, page)
            self.driver.get(page_link)

            first_time = True

            if page_link != self.driver.current_url:
                if first_time:
                    first_time = False
                else:
                    print('page link changed')
                    print(
                        f'the rest of the pages will be skipped {num_of_pages - page}')
                    return ids

            self.scroll_and_wait(0.2)
            src = self.driver.page_source
            soup = BeautifulSoup(src, "lxml")
            links = soup.find_all("a", {"class": "ads__item__ad--title"})
            links = [link.get('href') for link in links]
            ids.extend([link.replace('https://www.olx.com.eg/ad', '')
                        for link in links])
        return ids

    def run(self, start, end) -> pd.DataFrame:
        ads = []
        price = []
        location = []
        title = []
        date = []
        bedrooms = []
        area = []
        level = []
        bathrooms = []
        furnished = []
        type = []
        views = []
        description = []
        delivery_date = []
        compound = []
        amenities = []
        down_payment = []
        payment_option = []
        delivery_term = []
        owner_name = []
        owner_id = []
        ad_ids = []
        ids = self.get_links(start, end)
        if ids is None:
            return
        for id in tqdm(ids):
            ad = Ad(id)
            ads.append(ad)
        for ad in ads:
            ad_ids.append(ad.id)
            try:
                price.append(ad.price)
            except:
                price.append(np.nan)
            try:
                location.append(ad.location)
            except:
                location.append(np.nan)
            try:
                title.append(ad.title)
            except:
                title.append(np.nan)
            try:
                views.append(ad.views)
            except:
                views.append(np.nan)
            try:
                description.append(ad.description)
            except:
                description.append(np.nan)
            try:
                date.append(ad.date)
            except:
                date.append(np.nan)
            try:
                owner_name.append(ad.owner_name)
            except:
                owner_name.append('unknown')
            try:
                owner_id.append(ad.owner_id)
            except:
                owner_id.append(np.nan)

            ids.append(ad.id)

            if 'bedrooms' in ad.fields:
                bedrooms.append(ad.bedrooms)
            else:
                bedrooms.append(np.nan)
            if 'delivery_term' in ad.fields:
                delivery_term.append(ad.delivery_term)
            else:
                delivery_term.append(np.nan)
            if 'level' in ad.fields:
                level.append(ad.level)
            else:
                level.append(np.nan)
            if 'bathrooms' in ad.fields:
                bathrooms.append(ad.bathrooms)
            else:
                bathrooms.append(np.nan)
            if 'type' in ad.fields:
                type.append(ad.type)
            else:
                type.append(np.nan)
            if 'area_m' in ad.fields:
                area.append(ad.area_m)
            else:
                area.append(np.nan)
            if 'amenities' in ad.fields:
                amenities.append(ad.amenities)
            else:
                amenities.append(np.nan)
            if 'down_payment' in ad.fields:
                down_payment.append(ad.down_payment)
            else:
                down_payment.append(np.nan)
            if 'compound' in ad.fields:
                compound.append(ad.compound)
            else:
                compound.append(np.nan)
            if 'payment_option' in ad.fields:
                payment_option.append(ad.payment_option)
            else:
                payment_option.append(np.nan)
            if 'delivery_date' in ad.fields:
                delivery_date.append(ad.delivery_date)
            else:
                delivery_date.append(np.nan)
            if 'furnished' in ad.fields:
                furnished.append(ad.furnished)
            else:
                furnished.append(np.nan)

        return pd.DataFrame({
            'price': price,
            'location': location,
            'title': title,
            'bedrooms': bedrooms,
            'area': area,
            'level': level,
            'bathrooms': bathrooms,
            'furnished': furnished,
            'type': type,
            'delivery_date': delivery_date,
            'amenties': amenities,
            'down_payment': down_payment,
            'payment_option': payment_option,
            'compound': compound,
            'delivery_term': delivery_term,
            'views': views,
            'description': description,
            'date': date,
            'owner_name': owner_name,
            'owner_id': owner_id,
            'id': ad_ids
        })


OlxScraper(
    'apartments-duplex-for-sale',
    (0, 500000),
    30000,
    speed=State.FAST
)
