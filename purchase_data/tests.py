from django.test import TestCase
from .models import Item, PurchaseData

# Create your tests here.
class ItemModelTests(TestCase):
    def test_item_has_name(self):
        Item.objects.create(title='test_title', text='test_text')
        actual_item = Item.objects.get(title='test_title')
        self.assertIsInstance(actual_item.name, 'test_title')