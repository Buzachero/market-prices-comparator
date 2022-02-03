from openpyxl import load_workbook
from model.product import Product
import requests

def read_file():
    wb = load_workbook('input.xlsx')
    aba_ativa = wb['URLs Produtos']
    products_array = []
    i = 3
    while True:
        if aba_ativa.cell(row=i, column=1).value is None:
            break
        product = Product()
        product_attributes = []
        for j in range(1, 4):
            product_attributes.append(aba_ativa.cell(row=i, column=j).value)
        product.create(product_attributes[0], product_attributes[1], product_attributes[2])
        product_url = aba_ativa.cell(row=i, column=4).value
        product.add_market_info(aba_ativa.cell(row=1, column=4).value, product_url)
        if product_url is None:
            products_array.append(product)
            i = i + 1
            continue
        url = product.markets_info[0]['product_url']
        response = requests.get(url)
        availability = response.json()['availability']
        product.add_availability(0, availability)
        prices = response.json()['prices']
        for price in prices:
            product.add_price_info(0, price['minQuantity'], price['price'])
        products_array.append(product)
        i = i + 1
    return products_array
