
from login import Loginpage
from add_cart import Purchaseitem
from purchase import PlaceOrder
#from login import Loginpage
from driver_manager import Driver

driver_manager = Driver()
driver,wait = driver_manager.setup()
print('staring')
try:
    login = Loginpage(driver,wait)
    username_text = 'anoy_123'
    password_text = 'anoy123'
    login.login_ops(username_text,password_text)

    item = Purchaseitem(driver,wait)
    product_name_1 = 'Nexus 6'
    item.add_to_cart(product_name_1)
    product_name_2 = 'Samsung galaxy s6'
    item.add_to_cart(product_name_2)

    order = PlaceOrder(driver,wait)
    orders_count , orders = order.show_products()
    print("The Length of Orders are : ", orders_count)
    print("The Orders are : ", orders)



    order.place_order()
    #order.form_fill()

    customer_info = {
    'name': 'John Doe',
    'country': 'USA',
    'city': 'New York',
    'card': '123456789012',
    'month': '12',
    'year': '2026'
    } 

    order.form_fill(customer_info)
    


except Exception as e:
    print("The error :",e)

finally:
    driver_manager.teardown()
