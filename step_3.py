from data import products_string
from step_1 import transform_products_to_list
from pprint import pprint


def group_products_by_customer_and_invoice(products_string):
    products_list = transform_products_to_list(products_string)
    customers = {}
    
    for product in products_list:
        invoice = product[0]
        customer_id = product[-2]
        customers.setdefault(customer_id, {})
        customers[customer_id].setdefault(invoice, [])
        customers[customer_id][invoice].append(product)
    return customers
        