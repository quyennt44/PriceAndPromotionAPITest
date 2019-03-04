class Product:
    def __init__(self, supplier_sale_price=None, sell_price=None, pv_supported_price=None,
                 supplier_supported_price=None,
                 update_type=None, start_date=None, note=None):
        self.supplier_sale_price = supplier_sale_price
        self.sell_price = sell_price
        self.pv_supported_price = pv_supported_price
        self.supplier_supported_price = supplier_supported_price
        self.update_type = update_type
        self.start_date = start_date
        self.note = note

    # def __init__(self, supplier_sale_price=None, sell_price=None, pv_supported_price=None,
    #              supplier_supported_price=None):
    #     self.supplier_sale_price = supplier_sale_price
    #     self.sell_price = sell_price
    #     self.pv_supported_price = pv_supported_price
    #     self.supplier_supported_price = supplier_supported_price

    def __eq__(self, other):
        """Override the default Equals behavior"""
        return self.supplier_sale_price == other.supplier_sale_price \
            and self.sell_price == other.sell_price and self.pv_supported_price == other.pv_supported_price \
            and self.supplier_supported_price == other.supplier_supported_price \
            and self.update_type == other.update_type and self.start_date == other.start_date \
            and self.note == other.note

    def product_contain_same_value(product1, product2):
        if product1.supplier_sale_price == product2.supplier_sale_price \
                and product1.sell_price == product2.sell_price \
                and product1.pv_supported_price == product2.pv_supported_price \
                and product1.supplier_supported_price == product2.supplier_supported_price \
                and product1.update_type == product2.update_type \
                and product1.start_date == product2.start_date \
                and product1.note == product2.note:
            return True
        else:
            return False
