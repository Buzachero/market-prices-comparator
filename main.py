import excel_file_handler
from factory.market_factory import MarketFactory


def print_products_info(products_array):
    for product_element in products_array:
        print('-------------------------------------------------------------------------------------------------------')
        print(f'{product_element.code:3d} \
        | {product_element.name:60} \
        | {product_element.brand:15} \
        | {product_element.measure:20}')


def get_product_price(market_info):
    market_name = str.upper(market_info['market_name'])
    market = MarketFactory.get_market_instance(market_name)
    if market is None:
        return [{'min_quantity': 0, 'price': 0}]

    product_url = market_info['product_url']
    return market.get_price_info(product_url)


if __name__ == '__main__':
    products_array = excel_file_handler.read_products_from_file()
    print_products_info(products_array)
    for product in products_array:
        print(f'Processing product code {product.code} ...')
        for index in range(0, len(product.markets_info)):
            offers = get_product_price(product.markets_info[index])
            product.add_prices_info(index, offers)
    print()
