from pizzapi import *
import names
import json
import time
import argparse
from random import randint

def get_args():
    parser = argparse.ArgumentParser(description="Spams a Dominos location with orders")
    parser.add_argument("street",
                        help="Dominos to kill")
    parser.add_argument("city",
                        help="City where Dominos is")
    parser.add_argument("state",
                        help="State where Dominos is")
    parser.add_argument("zipcode",
                        help="Zipcode where Dominos is")
    return parser.parse_args()

def main():
    args = get_args()
	
    # Create Address object
    address = Address(args.street, args.city, args.state, args.zipcode)
    
    # Get closest store
    store = address.closest_store()
    menu = store.get_menu()

    while True:
        # Generate random contact info
        first = names.get_first_name()
        last = names.get_last_name()
        email = '{}{}@gmail.com'.format(first[0], last)
        phone = '256{}'.format(randint(1111111, 9999999))
        
        # Create Customer object
        customer = Customer(first, last, email, phone)
        print("{} {} {} {}".format(first, last, email, phone))

        # Create Order object, and add a pizza to the cart
        order = Order(store, customer, address)
        order.add_item('P16IBKZA') # add a 12-inch pan pizza

        # Place the order
        resp = order.place()
        print(resp['StatusItems'])

        time.sleep(5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Bye.")