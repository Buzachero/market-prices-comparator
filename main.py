import excel_file_handler

def print_products_info(products_array):
    for product in products_array:
        print('-------------------------------------------------------------------------------------------------------')
        print(f'NAME: {product.name}\nBRAND: {product.brand}\nWEIGHT/QUANTITY/VOLUME: {product.measure}')
        for market_info in product.markets_info:
            market_name = str.upper(market_info['market_name'])
            is_product_available = product.is_product_available(market_info['availability'])
            print(f'{market_name} ==> AVAILABLE: {is_product_available}')
            print('PRICES: ', end='')
            for offer in market_info['offers']:
                min_quantity = offer['min_quantity']
                price = offer['price']
                print(f'  R$ {price} ({min_quantity})', end='')
            print()

if __name__ == '__main__':
    products_array = excel_file_handler.read_file()
    print_products_info(products_array)




