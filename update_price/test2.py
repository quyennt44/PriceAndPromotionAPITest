import requests
import json
import random
import pprint
from update_price import common
from update_price import variables

PRODUCT_ID_FULL_INFORMATION = '1300856'


# TC_PP-368
# Set update_type = now
def test_update_full_data_with_update_type_is_now():
    url = variables.UPDATE_PRICE_URL + str(PRODUCT_ID_FULL_INFORMATION)

    # Get product information
    product_information = common.get_product_information_then_return_pared_data(url, variables.HEADERS)

    supplier_sale_price = common.get_product_field_value(product_information, variables.PRODUCT_DATA_PARENT_NODE,
                                                         variables.SUPPLIER_SALE_PRICE_PARAM_NAME)

    # assign new values
    new_pv_supported_price_value = random.randint(1, 1000)
    new_supplier_supported_price_value = random.randint(0, 2000)

    new_sell_price_value = supplier_sale_price - new_pv_supported_price_value - new_supplier_supported_price_value
    update_type = variables.UPDATE_TYPE_VALUE_NOW
    note = ''

    # data to send
    data = common.generate_data_form(new_sell_price_value, new_pv_supported_price_value,
                                     new_supplier_supported_price_value, update_type, note, None)
    print("data = " + str(data))

    # Send request
    response = requests.put(url, data=data, headers=variables.HEADERS);
    print("Response data = " + common.get_pretty_data(response, 4))

    product_form_response = json.loads(response.text);

    # get product information from response
    response_sell_price_value = common.get_product_field_value(product_form_response, variables.PRODUCT_DATA_PARENT_NODE,
                                                            variables.SELL_PRICE_PARAM_NAME)
    response_pv_supported_price_value = common.get_product_field_value(product_form_response,
                                                                    variables.PRODUCT_DATA_PARENT_NODE,
                                                                    variables.PV_SUPPORTED_PRICE_PARAM_NAME)
    response_supplier_supported_price_value = common.get_product_field_value(product_form_response,
                                                                          variables.PRODUCT_DATA_PARENT_NODE,
                                                                          variables.SUPPLIER_SUPPORT_PRICE_PARAM_NAME)

    # get product information after updated
    product_information = common.get_product_information_then_return_pared_data(url, variables.HEADERS)
    pprint.pprint("Data after updated = " + str(product_information))
    updated_sell_price_value = common.get_product_field_value(product_information, variables.PRODUCT_DATA_PARENT_NODE,
                                                               variables.SELL_PRICE_PARAM_NAME)
    updated_pv_supported_price_value = common.get_product_field_value(product_information,
                                                                       variables.PRODUCT_DATA_PARENT_NODE,
                                                                       variables.PV_SUPPORTED_PRICE_PARAM_NAME)
    updated_supplier_supported_price_value = common.get_product_field_value(product_information,
                                                                             variables.PRODUCT_DATA_PARENT_NODE,
                                                                             variables.SUPPLIER_SUPPORT_PRICE_PARAM_NAME)

    # assert
    assert response.status_code == 200
    assert new_pv_supported_price_value == response_pv_supported_price_value == updated_pv_supported_price_value
    assert new_supplier_supported_price_value == response_supplier_supported_price_value == updated_supplier_supported_price_value
    assert new_sell_price_value == response_sell_price_value == updated_sell_price_value


# TC_PP-370
# Set update_type = schedule
def test_update_full_data_with_update_type_is_schedule():
    print("dfdf")
    url = variables.UPDATE_PRICE_URL + str(PRODUCT_ID_FULL_INFORMATION)

    # Get product information
    product_information = common.get_product_information_then_return_pared_data(url, variables.HEADERS)

    supplier_sale_price = common.get_product_field_value(product_information, variables.PRODUCT_DATA_PARENT_NODE,
                                                         variables.SUPPLIER_SALE_PRICE_PARAM_NAME)

    # assign new values
    new_pv_supported_price_value = random.randint(1, 1000)
    new_supplier_supported_price_value = random.randint(0, 2000)

    new_sell_price_value = supplier_sale_price - new_pv_supported_price_value - new_supplier_supported_price_value
    update_type = variables.UPDATE_TYPE_VALUE_SCHEDULE
    # today = date.today()
    # start_date = today + random.randint(1,100)
    # print("start date = " + str(start_date))
    start_date = ''
    note = ''

    # data to send
    data = common.generate_data_form(new_sell_price_value, new_pv_supported_price_value,
                                     new_supplier_supported_price_value, update_type, note, start_date)
    print("data = " + str(data))

    # Send request
    response = requests.put(url, data=data, headers=variables.HEADERS);
    print("Response data = " + common.get_pretty_data(response, 4))

    product_form_response = json.loads(response.text);

    # get product information from response
    response_sell_price_value = common.get_product_field_value(product_form_response, variables.PRODUCT_DATA_PARENT_NODE,
                                                            variables.SELL_PRICE_PARAM_NAME)
    response_pv_supported_price_value = common.get_product_field_value(product_form_response,
                                                                    variables.PRODUCT_DATA_PARENT_NODE,
                                                                    variables.PV_SUPPORTED_PRICE_PARAM_NAME)
    response_supplier_supported_price_value = common.get_product_field_value(product_form_response,
                                                                          variables.PRODUCT_DATA_PARENT_NODE,
                                                                          variables.SUPPLIER_SUPPORT_PRICE_PARAM_NAME)

    # get product information after updated
    product_information = common.get_product_information_then_return_pared_data(url, variables.HEADERS)
    pprint.pprint("Data after updated = " + str(product_information))
    updated_sell_price_value = common.get_product_field_value(product_information, variables.PRODUCT_DATA_PARENT_NODE,
                                                               variables.SELL_PRICE_PARAM_NAME)
    updated_pv_supported_price_value = common.get_product_field_value(product_information,
                                                                       variables.PRODUCT_DATA_PARENT_NODE,
                                                                       variables.PV_SUPPORTED_PRICE_PARAM_NAME)
    updated_supplier_supported_price_value = common.get_product_field_value(product_information,
                                                                             variables.PRODUCT_DATA_PARENT_NODE,
                                                                             variables.SUPPLIER_SUPPORT_PRICE_PARAM_NAME)

    # assert
    assert response.status_code == 200
    assert new_pv_supported_price_value == response_pv_supported_price_value == updated_pv_supported_price_value
    assert new_supplier_supported_price_value == response_supplier_supported_price_value == updated_supplier_supported_price_value
    assert new_sell_price_value == response_sell_price_value == updated_sell_price_value

