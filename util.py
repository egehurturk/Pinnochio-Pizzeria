import requests
import os
from bs4 import BeautifulSoup
import asyncio
import aiohttp
import functools
import time
from orders.models import *

# .foodmenu, .toppingmenu,
# [] -> foodmenu, [] -> toppingmenu


class Scraper:

    def __init__(self, url="http://www.pinocchiospizza.net/menu.html", file_="content"):
        self.url = url
        self.file_ = file_

    def get_response(self) -> requests.Response:
        """
        Makes the GET Request for the specified URL.
            :return:
                request.Response: The request object.
        """

        response = requests.get(self.url)
        response.raise_for_status()
        return response

    def parse(self, response: requests.Response):
        """
        Parses the request.
        :param response: request.Response, the request object
        :return: elems_food, elems_toppings
        """
        soup = BeautifulSoup(response.text, 'html.parser')
        self.elems_food = soup.select("table.foodmenu > tbody > tr")
        self.elems_toppings = soup.select("table.toppingmenu > tbody > tr")
        return self.elems_food, self.elems_toppings

    def save_to_file(self) -> None:
        """
        Saves the parsed objects to file.
        :return: None
        """
        if not os.path.exists(os.getcwd() + "/utilcontent"):
            os.makedirs(os.getcwd() + "/utilcontent")

        with open(f'utilcontent/{self.file_}_food.txt', 'w+') as f:
            with open(f'utilcontent/{self.file_}_topping.txt', 'w+') as t:
                f.write(str(self.elems_food))
                t.write(str(self.elems_toppings))

        print('Saved to file!')



if __name__ == '__main__':
    scraper = Scraper()
    response = scraper.get_response()
    f, t = scraper.parse(response)
    start_time = time.time()
    scraper.save_to_file()
    print("--- %s seconds ---" % (time.time() - start_time))