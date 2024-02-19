from django.test import TestCase
from erp_core.models import Category, Product, Client, Sale, SaleDetail

class ModelTest(TestCase):
    def test_model_creation(self):
        # Create Category
        category = Category.objects.create(name='Electronics')
        self.assertTrue(isinstance(category, Category))
        self.assertEqual(str(category), 'Electronics')

        # Create Product
        product = Product.objects.create(name='Laptop', category=category)
        self.assertTrue(isinstance(product, Product))
        self.assertEqual(str(product), f"{product.name} | ${product.pvp} | {product.stock} ud(s)")

        # Create Client
        client = Client.objects.create(identity_card_number='1234567890', first_name='John', last_name='Doe')
        self.assertTrue(isinstance(client, Client))
        self.assertEqual(str(client), f"{client.identity_card_number} | {client.first_name}  {client.last_name}")

        # Create Sale
        sale = Sale.objects.create(client=client)
        self.assertTrue(isinstance(sale, Sale))

        # Create SaleDetail
        sale_detail = SaleDetail.objects.create(sale=sale, product=product, amount=1)
        self.assertTrue(isinstance(sale_detail, SaleDetail))

