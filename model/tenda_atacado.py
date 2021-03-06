from model.market import Market
import requests


class TendaAtacado(Market):
    _instance = None

    def __init__(self):
        self.name = "TENDA ATACADO"

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
        response = requests.get(url)
        offers = []
        if response.status_code == 200:
            prices = response.json()['prices']
            for price in prices:
                offer = {}
                offer['min_quantity'] = price['minQuantity']
                offer['price'] = super().format_price(price['price'])
                offers.append(offer)
        return offers