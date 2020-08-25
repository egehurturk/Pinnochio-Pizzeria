import requests
import os
import sys
from bs4 import BeautifulSoup
import pprint

__all__ = ['Scraper']
# .foodmenu, .toppingmenu,
# [] -> foodmenu, [] -> toppingmenu

class Scraper:


    def __init__(self, url, file_):
        self.url = url
        self.file_ = file_

    def get_response(self) -> requests.Response:
        response = requests.get(self.url)
        response.raise_for_status()
        return response

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        self.elems_food = soup.select("table.foodmenu > tbody > tr")
        self.elems_toppings = soup.select("table.toppingmenu > tbody > tr")
        return self.elems_food, self.elems_toppings


    def save_to_file(self):
        try:
            with open(f'utilcontent/{self.file_}_food.txt', 'w') as f:
                f.write(pprint.pprint(str(self.elems_food)))

            with open(f'utilcontent/{self.file_}_topping.txt', 'w') as t:
                t.write(pprint.pprint(str(self.elems_toppings)))

            print('Saved to file!')
        except FileNotFoundError:
            print('File cannot be found')
        except IOError:
            print('File cannot be found. Enter a valid file name.')
