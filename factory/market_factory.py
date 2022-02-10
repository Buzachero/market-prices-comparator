from model.jau_serve import JauServe
from model.tenda_atacado import TendaAtacado


class MarketFactory:
    @classmethod
    def get_market_instance(cls, market_name):
        tenda_atacado = TendaAtacado.get_instance()
        jau_serve = JauServe.get_instance()
        if market_name == tenda_atacado.get_name():
            return tenda_atacado
        elif market_name == jau_serve.get_name():
            return jau_serve

        return None
