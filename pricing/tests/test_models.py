from django.test import TestCase
from pricing.models import Organization, Item, Pricing

class PricingModelTestCase(TestCase):
    def setUp(self):
        self.org = Organization.objects.create(name='Test Organization')
        self.item = Item.objects.create(type='perishable', description='Test Item')
        self.pricing = Pricing.objects.create(
            organization=self.org,
            item=self.item,
            zone='Test Zone',
            base_distance_in_km=10,
            km_price=1.5,
            fix_price=10
        )

    def test_pricing_representation(self):
        expected_representation = f"{self.org.name} - {self.item.description} - Test Zone"
        self.assertEqual(str(self.pricing), expected_representation)
