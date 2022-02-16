from model.market import Market
import requests

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


class JauServe(Market):
    _instance = None

    def __init__(self):
        self.name = "JAU SERVE"

    def get_name(self):
        return self.name

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def get_price_info(self, url):
        if url is None:
            return []

        product_obj = requests.get(url)
        html = product_obj.content.decode("utf-8")
        parsed_html = BeautifulSoup(html, features="html.parser")
        value = parsed_html.body.find('span', attrs={'class': 'sales mr-2'}).text

        offer = {}
        price_currency = value.strip()
        if price_currency is None \
                or not price_currency.startswith("R$"):
            return offer

        price_tokens = price_currency.split(' ')

        if len(price_tokens) != 2:
            return offer

        offer['min_quantity'] = 1
        offer['price'] = super().format_price(price_tokens[1])

        return [offer]
