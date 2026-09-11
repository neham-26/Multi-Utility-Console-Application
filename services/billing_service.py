# Billing_service.py
def run_student_module():
 print("Billing module is under construction.")

"""Product bill generation."""

from models.product import Product
from services.input_utils import read_text, read_float, read_int


class ProductBilling:
    def __init__(self, product, discount_pct, tax_pct):
        self.__product = product
        self.__discount_pct = discount_pct
        self.__tax_pct = tax_pct

    def calculate_gross(self):
        p = self.__product
        return p.get_quantity() * p.get_unit_price()

    def calculate_discount_amount(self):
        return self.calculate_gross() * self.__discount_pct / 100

    def calculate_amount_after_discount(self):
        return self.calculate_gross() - self.calculate_discount_amount()

    def calculate_tax_amount(self):
        return (
            self.calculate_amount_after_discount()
            * self.__tax_pct
            / 100
        )

    def calculate_final_amount(self):
        return (
            self.calculate_amount_after_discount()
            + self.calculate_tax_amount()
        )

    def display_bill(self):
        p = self.__product

        print()
        print("=" * 40)
        print(" PRODUCT BILL")
        print("=" * 40)

        print(f"Product ID    : {p.get_product_id()}")
        print(f"Name          : {p.get_name()}")
        print(f"Category      : {p.get_category()}")
        print(f"Quantity      : {p.get_quantity()}")
        print(f"Unit Price    : {p.get_unit_price():.2f}")
        print(f"Gross Amount  : {self.calculate_gross():.2f}")
        print(
            f"Discount ({self.__discount_pct:.2f}%) : "
            f"{self.calculate_discount_amount():.2f}"
        )
        print(
            f"After Discount : "
            f"{self.calculate_amount_after_discount():.2f}"
        )
        print(
            f"Tax ({self.__tax_pct:.2f}%) : "
            f"{self.calculate_tax_amount():.2f}"
        )
        print(f"FINAL BILL    : {self.calculate_final_amount():.2f}")

        print("=" * 40)


def run_billing_module():
    product_id = read_text("Product ID: ")
    name = read_text("Product name: ")
    category = read_text("Category: ")

    while True:
        quantity = read_int("Quantity: ")

        if quantity > 0:
            break

        print("Error: quantity must be greater than zero.")

    while True:
        unit_price = read_float("Unit price: ")

        if unit_price > 0:
            break

        print("Error: unit price must be greater than zero.")

    while True:
        discount = read_float("Discount percentage (0-100): ")

        if 0 <= discount <= 100:
            break

        print("Error: discount must be between 0 and 100.")

    while True:
        tax = read_float("Tax percentage: ")

        if tax >= 0:
            break

        print("Error: tax cannot be negative.")

    product = Product(
        product_id,
        name,
        category,
        quantity,
        unit_price
    )

    billing = ProductBilling(
        product,
        discount,
        tax
    )

    billing.display_bill()