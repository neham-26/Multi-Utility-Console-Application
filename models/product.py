"""Product data."""


class Product:
    def __init__(self, product_id, name, category, quantity, unit_price):
        self.__product_id = product_id
        self.__name = name
        self.__category = category
        self.__quantity = quantity
        self.__unit_price = unit_price

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_category(self):
        return self.__category

    def get_quantity(self):
        return self.__quantity

    def get_unit_price(self):
        return self.__unit_price