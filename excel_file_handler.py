import openpyxl
import os
import time_handler
from openpyxl import load_workbook
from model.product import Product

WITHOUT_URL_MSG = 'SEM URL'
OUTPUT_DIR = "output"


def read_products_from_file():
    wb = load_workbook('input.xlsx')
    active_workbook = wb['URLs Produtos']
    market_names = get_market_names(active_workbook)
    products_array = []
    i = 3
    # while True:
    while i < 9:
        if active_workbook.cell(row=i, column=1).value is None:
            break
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


def write_products_to_file(products_array):
    wb = openpyxl.Workbook()
    sheet = wb.active
    j = 5
    market_names = products_array[0].get_market_names()
    for market_name in market_names:
        market_name_cell = sheet.cell(row=1, column=j)
        market_name_cell.value = str.upper(market_name)
        j = j + 1

    sheet.cell(row=2, column=1).value = "Código"
    sheet.cell(row=2, column=2).value = "Item"
    sheet.cell(row=2, column=3).value = "Peso/Quantidade/Volume"
    sheet.cell(row=2, column=4).value = "Marca"
    j = 5
    for index in range(0, len(market_names)):
        sheet.cell(row=2, column=j).value = "Preço Unitário (R$)"
        j = j + 1

    i = 3
    for product in products_array:
        sheet.cell(row=i, column=1).value = product.code
        sheet.cell(row=i, column=2).value = product.name
        sheet.cell(row=i, column=3).value = product.measure
        sheet.cell(row=i, column=4).value = product.brand
        j = 5
        for market_info in product.markets_info:
            if market_info['product_url'] is None:
                sheet.cell(row=i, column=j).value = WITHOUT_URL_MSG
            else:
                price = '{:.2f}'.format(float(market_info['offers'][0][0]['price']))
                sheet.cell(row=i, column=j).value = price
            j = j + 1
        i = i + 1

    current_path = os.getcwd()
    output_path = os.path.join(current_path, OUTPUT_DIR)
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    file_name = "OUTPUT_" + time_handler.get_now_time() + ".xlsx"
    output_file = os.path.join(output_path, file_name)
    wb.save(output_file)
    print(f'Excel file {output_file} was successfully generated!')


