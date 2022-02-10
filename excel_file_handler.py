from openpyxl import load_workbook
from model.product import Product


def read_products_from_file():
    wb = load_workbook('input.xlsx')
    active_workbook = wb['URLs Produtos']
    market_names = get_market_names(active_workbook)
    products_array = []
    i = 3
    while True:
        if active_workbook.cell(row=i, column=1).value is None:
            break
        # product = Product()
        product_attributes = []
        for j in range(1, 5):
            product_attributes.append(active_workbook.cell(row=i, column=j).value)
        product = Product(product_attributes[0], product_attributes[1], product_attributes[2], product_attributes[3])

        for j in range(5, 5+len(market_names)):
            product_url = active_workbook.cell(row=i, column=j).value
            product.add_market_info(market_names[j-5], product_url)

        products_array.append(product)
        i = i + 1
    return products_array


def get_market_names(active_workbook):
    market_names = []
    for col in range(5,11):
        market_name = active_workbook.cell(row=1, column=col).value
        if market_name is not None:
            market_names.append(market_name)
        else:
            break

    return market_names


