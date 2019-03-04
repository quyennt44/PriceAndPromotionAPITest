import requests
from update_price import variables
from update_price import Product
import json


def get_product_information_then_return_pared_data(url, headers):
    response = requests.get(url, headers = headers)
    # response = requests.get(variables.UPDATE_PRICE_URL + str(product_id), headers=variables.HEADERS)
    # pretty_data = json.dumps(response.json(), indent=4)
    # print(pretty_data);
    #
    # parsed = json.loads(response.text)
    # # print(parsed)
    # print("Sell_price = " + str(parsed["data"]["sell_price"]))
    # print("product_line_id = " + str(parsed["data"]["product_line_id"]))
    parsed = json.loads(response.text)
    return parsed


def get_pretty_data(data, indent):
    pretty_data = json.dumps(data.json(), indent=indent)
    return pretty_data


def get_parsed_data(data):
    parsed = json.loads(data.text)
    return parsed


def get_product_field_value(parsed_data, parent_node, field_name):
    value = parsed_data[parent_node][field_name]
    return value;

# def test_get_product():
#     response = get_product_information(PRODUCT_ID_FULL_INFORMATION);
#     print(response)

# def generate_input_data(param_name_list, param_value_list):
#     #do thing to build input here
#     return input_form;


def put_request_then_return_parsed_data(url, data, headers):
    response = requests.put(url, data=data, headers=headers);
    parsed = json.loads(response.text)
    return parsed;


def generate_data_form(sell_price, pv_support_price, supplier_support_price, update_type, note, start_date):
        # build data input form
        data = variables.DATA_FORM_WITH_START_DATE

        data[variables.SELL_PRICE_PARAM_NAME] = sell_price
        data[variables.UPDATE_TYPE_PARAM_NAME] = update_type
        data[variables.PV_SUPPORTED_PRICE_PARAM_NAME] = pv_support_price
        data[variables.SUPPLIER_SUPPORT_PRICE_PARAM_NAME] = supplier_support_price
        data[variables.NOTE_PARAM_NAME] = note

        if start_date is None:
            del data[variables.START_DATE_PARAM_NAME]
        else:
            data[variables.START_DATE_PARAM_NAME] = start_date

        return data


def generate_product_information(product_information):
    # product_information = get_product_information_then_return_pared_data(url, headers)
    # print("Product info:" + str(product_information))

    # supplier_sale_price_value = get_product_field_value(product_information, variables.PRODUCT_DATA_PARENT_NODE,
    #                                                       variables.SUPPLIER_SALE_PRICE_PARAM_NAME)
    sell_price_value = get_product_field_value(product_information, variables.PRODUCT_DATA_PARENT_NODE,
                                                          variables.SELL_PRICE_PARAM_NAME)
    pv_supported_price_value = get_product_field_value(product_information,
                                                                  variables.PRODUCT_DATA_PARENT_NODE,
                                                                  variables.PV_SUPPORTED_PRICE_PARAM_NAME)
    supplier_supported_price_value = get_product_field_value(product_information,
                                                                        variables.PRODUCT_DATA_PARENT_NODE,
                                                                        variables.SUPPLIER_SUPPORT_PRICE_PARAM_NAME)

    # update_type_value = get_product_field_value(product_information, variables.PRODUCT_DATA_PARENT_NODE,
    #                                                      variables.UPDATE_TYPE_PARAM_NAME)
    #
    # start_date_value = get_product_field_value(product_information, variables.PRODUCT_DATA_PARENT_NODE,
    #                                       variables.START_DATE_PARAM_NAME)
    #
    # note_value = get_product_field_value(product_information, variables.PRODUCT_DATA_PARENT_NODE,
    #                                      variables.NOTE_PARAM_NAME)

    product = Product.Product()
    # product.supplier_sale_price = supplier_sale_price_value
    product.sell_price = sell_price_value
    product.pv_supported_price = pv_supported_price_value
    product.supplier_supported_price = supplier_supported_price_value
    # product.update_type = update_type_value
    # product.start_date = start_date_value
    # product.note = note_value

    print("sell price = " + str(product.sell_price))
    return product



