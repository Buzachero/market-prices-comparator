class Product(object):
    def __init__(self, code, name, measure, brand):
        self.code = code
        self.name = name
        self.measure = measure
        self.brand = brand
        self.markets_info = []

    def add_market_info(self, market_name, product_url):
        market_info = {}
        market_info['market_name'] = market_name
        market_info['product_url'] = product_url
        market_info['offers'] = []
        self.markets_info.append(market_info)

    def add_prices_info(self, index, offers):
        if index >= len(self.markets_info):
            return
        self.markets_info[index]['offers'].append(offers)

    def add_price_info(self, index, min_quantity, price):
        if index >= len(self.markets_info):
            return
        offer = {}
        offer['min_quantity'] = min_quantity
        offer['price'] = price
        self.markets_info[index]['offers'].append(offer)

    def get_market_names(self):
        market_names = []
        for market_info in self.markets_info:
            market_names.append(market_info['market_name'])
        return market_names

    def add_availability(self, index, availability):
        if index >= len(self.markets_info):
            return
        self.markets_info[index]['availability'] = availability

    def is_product_available(self, availability):
        if availability is None:
            return False
        elif availability == 'in_stock':
            return True
        else:
            return False
