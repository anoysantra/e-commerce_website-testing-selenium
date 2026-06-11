import json
import pytest
import os
from operations.login import Loginpage

base_path = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the JSON file
# '..' means "go up one level" out of the test folder, then into test-data
json_path = os.path.join(base_path, '..', 'test-data', 'creds_data.json')

print(f"DEBUG: Looking for file at: {json_path}")

with open(json_path) as f:
    data = json.load(f)
    creds_data = data['login_credentials']

#print(creds_data)


@pytest.mark.parametrize('username,password',creds_data)
def test_login_ops(driver_setup,username,password):
    driver,wait = driver_setup
    login_instance = Loginpage(driver,wait)
    username_text = login_instance.login_ops(username,password)
    assert username_text.strip() == f'Welcome {username}'





