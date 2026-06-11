"""
data = {
  "shopping_items": [
    { "product_name": "Samsung galaxy s6" },
    { "product_name": "Nokia lumia 1520" },
    { "product_name": "Nexus 6" },
    { "product_name": "Samsung galaxy s7" },
    { "product_name": "Iphone 6 32gb" }
  ]
}

items = data['shopping_items']
items_data = []
for item in items:
    value = item["product_name"]
    row = (value,)
    items_data.append(row)

print(items_data)
"""
username = 'anoy_123'
if username.strip() == 'anoy_123':
    print("Same")


{
  "login_credentials": [
    ["standard_user_123", "password123"],
    ["test_user_abc", "wrong_pass"],
    ["another_user", "pass_999"],
    ["anoy_123","anoy123"]
  ]
}

