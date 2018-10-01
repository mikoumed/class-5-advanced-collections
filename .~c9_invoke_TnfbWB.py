from data import products_string
from step_1 import transform_products_to_list
from pprint import pprint


def calculate_total_per_invoices(products_string):
    products_list = transform_products_to_list(products_string)
    customers = {}
    
    for product in products_list:
        invoice = product[0]
        customer_id = product[-2]
        quantity = int(product[3])
        unit_price = float(product[-3])
        total = round(quantity*unit_price,2)
        
        customers.setdefault(customer_id, {})
        customers[customer_id].setdefault(invoice, 0)
        print(c
        customers[customer_id][invoice] += total
        
    return customers
    
pprint(calculate_total_per_invoices(products_string))
