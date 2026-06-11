
import json
import pytest
import os
from operations.add_cart import Purchaseitem
from operations.purchase import PlaceOrder

base_path = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the JSON file
# '..' means "go up one level" out of the test folder, then into test-data
json_path = os.path.join(base_path, '..', 'test-data','product_data.json')

print(f"DEBUG: Looking for file at: {json_path}")


with open(json_path) as f:
    data = json.load(f)
    items = data["shopping_items"]

items_data = []
for item in items:
    value = item["product_name"]
    items_data.append(value)

print(items_data)




@pytest.mark.parametrize('product_name',items_data)
def test_add_to_cart(keep_logged_in,product_name):
    driver,wait = keep_logged_in
    item = Purchaseitem(driver,wait)
    text = item.add_to_cart(product_name)
    assert text == 'item accepted'

def test_show_products(keep_logged_in):
    driver,wait = keep_logged_in
    orders = PlaceOrder(driver,wait)
    count, products = orders.show_products()
    print("dEBUG: ",products)
    print("The no of count : ",count)
    assert count >= 4

def test_form_fill(keep_logged_in):
    driver,wait = keep_logged_in
    order = PlaceOrder(driver,wait)
    order.place_order()
    customer_data ={
    'name': 'John Doe',
    'country': 'USA',
    'city': 'New York',
    'card': '123456789012',
    'month': '12',
    'year': '2026'
    } 
    msg = order.form_fill(customer_data)
    print(msg)
    assert msg.strip() =="Thank you for your purchase!"







