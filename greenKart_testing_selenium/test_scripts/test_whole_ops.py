import pytest
import json
from operations.select_vegetable import SelectVegetable
from operations.promo_code import PromoCode
from operations.show_total import ShowTotal
from operations.product_table import ProductTable


with open('test_data/test_data.json') as f:
    test_data = json.load(f)
    vegetables = test_data["vegetable_sets"]


@pytest.mark.parametrize("vegetable_names",vegetables)
def test_end_to_end(driver,vegetable_names):

    select = SelectVegetable(driver)
    url = select.select_vegetable(vegetable_names)
    assert url.strip() == "https://rahulshettyacademy.com/seleniumPractise/#/cart","Not added to Cart"

    product = ProductTable(driver)
    count_vegetable = product.product_table_display()
    count_test_data = len(vegetable_names)
    assert count_vegetable == count_test_data,"Count Not Similar"

    
    promo = PromoCode(driver)
    promo_msg = promo.promo_code("rahulshettyacademy")
    assert promo_msg.strip() == "Code applied ..!", "Promo Code not applied"

    total_show = ShowTotal(driver)
    gross_total, discount , total = total_show.show_total()
    total = float(total)
    gross_total = float(gross_total)
    expected_gross = round(total * 0.90, 2)
    assert discount.strip() == '10%'
    assert expected_gross == gross_total,"Total Not Matching"


    
