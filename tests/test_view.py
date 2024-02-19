from django.test import TestCase
from django.urls import reverse
from erp_core.models import Category, Product
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission  

class CategoryAndProductViewPermissionTests(TestCase):
    def setUp(self):
        # Create test data for each model
        self.category = Category.objects.create(name='Electronics')
        self.product = Product.objects.create(name='Laptop', category=self.category)

        # Create user
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # user permissions
        self.user.user_permissions.add(
            Permission.objects.get(codename='view_category'),
            Permission.objects.get(codename='view_product')
        )

    def test_category_list_view(self):
        response = self.client.get(reverse('erp:category-list'))
        self.assertEqual(response.status_code,   200)  
        self.assertTemplateUsed(response, 'erp_core/category_list.html')
        self.assertContains(response, self.category.name)

    def test_product_list_view(self):
        response = self.client.get(reverse('erp:product-list'))
        self.assertEqual(response.status_code,   200)  
        self.assertTemplateUsed(response, 'erp_core/product_list.html')
        self.assertContains(response, self.product.name)
