def transform_products_to_list(products_string):
    
    products_string_splitted = products_string.split('\n')
    
    product_list = []
    
    for product in products_string_splitted:
        if product:
            product_list.append(product.split(','))
    return product_list
