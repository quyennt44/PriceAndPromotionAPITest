import requests
from update_price import variables

PRODUCT_ID_FULL_INFORMATION = '18120188'

def get_product_information(product_id):
    response = requests.get(variables.UPDATE_PRICE_URL + str(product_id), headers = variables.HEADERS)
    return response



def test_get_product():
    get_product_information(PRODUCT_ID_FULL_INFORMATION);

# def test_update_when_sell_price_null(prduct_id):
#     response = requests.put(variables.UPDATE_PRICE_URL + str(prduct_id));
#     # response.json();
#     print(response.status_code);
#     print(response.content);
#
#     assert response.status_code == 200;




