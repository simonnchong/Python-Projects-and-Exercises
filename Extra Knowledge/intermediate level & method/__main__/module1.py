def calculate_tax(price, tax):
    return price * tax

def print_billing_doc():
    tax_rate = 0.1
    products = [{'name': 'Book',  'price': 30},
                {'name': 'Pen', 'price': 5}]

    # print billing header
    print(f'Name\tPrice\tTax')

    # print the billing item
    for product in products:
        tax = calculate_tax(product['price'], tax_rate)
        print(f"{product['name']}\t{product['price']}\t{tax}")

def print_hello_world():
    print("Hello World")

if __name__ == "__main__":
    print(__name__)
    print_billing_doc()
else:
    print_hello_world()