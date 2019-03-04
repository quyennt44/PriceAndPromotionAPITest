ACCESS_TOKEN_VALUE = 'tester_token@123'

HEADERS = {"Authorization": "Bearer " + ACCESS_TOKEN_VALUE}

UPDATE_PRICE_URL = 'https://dev-ppm.phongvu.vn/api/products/'

PRODUCT_DATA_PARENT_NODE = 'data'

SELL_PRICE_PARAM_NAME = 'sell_price'
PV_SUPPORTED_PRICE_PARAM_NAME = 'pv_supported_price'
SUPPLIER_SUPPORT_PRICE_PARAM_NAME = 'supplier_supported_price'
UPDATE_TYPE_PARAM_NAME = 'update_type'
START_DATE_PARAM_NAME = 'start_date'
NOTE_PARAM_NAME = 'note'

UPDATE_TYPE_VALUE_NOW = 'UPDATE_NOW'
UPDATE_TYPE_VALUE_SCHEDULE = 'SET_SCHEDULE'

SUPPLIER_SALE_PRICE_PARAM_NAME = 'supplier_sale_price'


DATA_FORM_WITHOUT_START_DATE = {
                SELL_PRICE_PARAM_NAME: 0,
                PV_SUPPORTED_PRICE_PARAM_NAME: 0,
                SUPPLIER_SUPPORT_PRICE_PARAM_NAME: 0,
                UPDATE_TYPE_PARAM_NAME: '',
                NOTE_PARAM_NAME: ''
            }

DATA_FORM_WITH_START_DATE = {
                SELL_PRICE_PARAM_NAME: 0,
                PV_SUPPORTED_PRICE_PARAM_NAME: 0,
                SUPPLIER_SUPPORT_PRICE_PARAM_NAME: 0,
                UPDATE_TYPE_PARAM_NAME: '',
                START_DATE_PARAM_NAME: 0,
                NOTE_PARAM_NAME: ''
            }

