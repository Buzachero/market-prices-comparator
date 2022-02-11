import excel_file_handler
from factory.market_factory import MarketFactory

PROD_CODE_TAB = 3
PROD_NAME_TAB = 60
PROD_BRAND_TAB = 15
PROD_MEASURE_TAB = 10

WITHOUT_URL_MSG = 'SEM URL'


def print_products_info(products_info_array):
    initial_tab = PROD_CODE_TAB + PROD_NAME_TAB + PROD_BRAND_TAB + PROD_MEASURE_TAB + 3 * 3
    print('-' * initial_tab)
    for product_element in products_info_array:
        print(f'{product_element.code:{PROD_CODE_TAB}} | {product_element.name:{PROD_NAME_TAB}} | {product_element.brand:{PROD_BRAND_TAB}} | {product_element.measure:{PROD_MEASURE_TAB}}')


def get_product_price(market_info):
    market_name = str.upper(market_info['market_name'])
    market = MarketFactory.get_market_instance(market_name)
    if market is None:
        return [{'min_quantity': 0, 'price': 0}]

    product_url = market_info['product_url']
    return market.get_price_info(product_url)


def show_menu_header():
    print('--------------------------------------------------------------')
    print('##############################################################')
    print('                             MENU                             ')
    print('##############################################################')


def show_menu():
    show_menu_header()
    while True:
        show_menu_1()
        choice_menu_1 = input('X: ')
        if not is_int(choice_menu_1):
            continue
        int_menu_1 = int(choice_menu_1)
        if int_menu_1 < 1 or int_menu_1 > 3:
            continue
        if int_menu_1 == 2 or int_menu_1 == 3:
            print('\nGood bye!')
            exit(0)
        break

    print()


def show_menu_1():
    print('\nWhat action do you want to take?')
    print('1) Get prices from all products')
    print('2) Choose from which products to get the prices')
    print('3) Exit')


def get_prices(products):
    for product in products:
        print(f'Processing product code {product.code} ...')
        for index in range(0, len(product.markets_info)):
            offers = get_product_price(product.markets_info[index])
            product.add_prices_info(index, offers)


def show_prices(products):
    initial_tab = PROD_CODE_TAB + PROD_NAME_TAB + PROD_BRAND_TAB + PROD_MEASURE_TAB + 3*3
    print(' ' * initial_tab, end='')
    max_length_name = 0
    for name in products[0].get_market_names():
        print(f' | {str.upper(name)}', end='')
        if len(name) > max_length_name:
            max_length_name = len(name)
    print()
    print('-' * initial_tab + '-' *max_length_name*2, end='')
    for product in products:
        print()
        print(f'{product.code:{PROD_CODE_TAB}} | {product.name:{PROD_NAME_TAB}} | {product.brand:{PROD_BRAND_TAB}} | {product.measure:{PROD_MEASURE_TAB}}', end='')
        for market_info in product.markets_info:
            if market_info['product_url'] is None:
                print(f' | {WITHOUT_URL_MSG:{max_length_name-len(WITHOUT_URL_MSG)}}', end='')
            else:
                price = '{:.2f}'.format(float(market_info['offers'][0][0]['price']))
                print(f' | R$ {price:{max_length_name-3}}', end='')


def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    products_array = excel_file_handler.read_products_from_file()
    print_products_info(products_array)
    show_menu()
    get_prices(products_array)
    show_prices(products_array)
    print()
