from behave import given
from service.models import Product

@given("the following products")
def step_impl(context):
    """Load background data into the system before each scenario"""
    # First, clear all products
    Product.delete_all()

    # Then, iterate over the rows in the context.table
    for row in context.table:
        product = Product()
        product.id = None
        product.name = row["name"]
        product.description = row["description"]
        product.price = float(row["price"])
        product.available = row["available"].lower() == "true"
        product.category = row["category"]
        product.create()
