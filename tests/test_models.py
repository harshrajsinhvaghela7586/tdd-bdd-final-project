import unittest
from service.models import Product
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):

    def setUp(self):
        """Runs before each test"""
        Product.delete_all()  # Ensure clean database for each test

    def test_create_product(self):
        """Test creating a product"""
        product = ProductFactory()
        product.id = None
        product.create()
        self.assertIsNotNone(product.id)

    def test_read_product(self):
        """Test reading a product"""
        product = ProductFactory()
        product.id = None
        product.create()

        found = Product.find(product.id)
        self.assertEqual(found.id, product.id)
        self.assertEqual(found.name, product.name)
        self.assertEqual(found.description, product.description)
        self.assertEqual(found.price, product.price)
        self.assertEqual(found.available, product.available)
        self.assertEqual(found.category, product.category)

    def test_update_product(self):
        """Test updating a product"""
        product = ProductFactory()
        product.id = None
        product.create()

        original_id = product.id
        product.description = "Updated description"
        product.update()

        updated = Product.find(original_id)
        self.assertEqual(updated.id, original_id)
        self.assertEqual(updated.description, "Updated description")
        self.assertEqual(len(Product.all()), 1)

    def test_delete_product(self):
        """Test deleting a product"""
        product = ProductFactory()
        product.id = None
        product.create()
        self.assertEqual(len(Product.all()), 1)

        product.delete()
        self.assertEqual(len(Product.all()), 0)

    def test_list_all_products(self):
        """Test listing all products"""
        self.assertEqual(len(Product.all()), 0)
        for _ in range(5):
            product = ProductFactory()
            product.id = None
            product.create()

        self.assertEqual(len(Product.all()), 5)

    def test_find_by_name(self):
        """Test finding products by name"""
        products = [ProductFactory() for _ in range(5)]
        for p in products:
            p.id = None
            p.create()

        name_to_search = products[0].name
        found = Product.find_by_name(name_to_search)
        expected_count = sum(1 for p in products if p.name == name_to_search)

        self.assertEqual(len(found), expected_count)
        for f in found:
            self.assertEqual(f.name, name_to_search)

    def test_find_by_availability(self):
        """Test finding products by availability"""
        products = [ProductFactory() for _ in range(10)]
        for p in products:
            p.id = None
            p.create()

        avail_to_search = products[0].available
        found = Product.find_by_availability(avail_to_search)
        expected_count = sum(1 for p in products if p.available == avail_to_search)

        self.assertEqual(len(found), expected_count)
        for f in found:
            self.assertEqual(f.available, avail_to_search)

    def test_find_by_category(self):
        """Test finding products by category"""
        products = [ProductFactory() for _ in range(10)]
        for p in products:
            p.id = None
            p.create()

        category_to_search = products[0].category
        found = Product.find_by_category(category_to_search)
        expected_count = sum(1 for p in products if p.category == category_to_search)

        self.assertEqual(len(found), expected_count)
        for f in found:
            self.assertEqual(f.category, category_to_search)


if __name__ == "__main__":
    unittest.main()
