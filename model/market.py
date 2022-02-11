import abc


class Market(object):

    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def get_price_info(self, url):
        pass

    def format_price(self, price):
        return str(price).replace(',', '.')
