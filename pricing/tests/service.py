from django.test import TestCase
from pricing.models import Pricing
from pricing.services import PriceCalculator

class PriceCalculatorTest(TestCase):
    def setUp(self):
        self.organization_id = 1
        self.zone = 'ZoneA'
        self.base_distance = 5
        self.base_price = 10
        self.per_km_price = 2

        Pricing.objects.create(
            organization_id=self.organization_id,
            zone=self.zone,
            base_distance_in_km=self.base_distance,
            fix_price=self.base_price,
            km_price=self.per_km_price,
            item_id=1
        )

    def test_calculate_total_price_within_base_distance(self):
        total_distance = 3
        item_type = 'perishable'
        total_price = PriceCalculator.calculate_total_price(self.zone, self.organization_id, total_distance, item_type)
        expected_price = self.base_price
        self.assertEqual(total_price, expected_price)

    def test_calculate_total_price_outside_base_distance(self):
        total_distance = 8
        item_type = 'non-perishable'
        total_price = PriceCalculator.calculate_total_price(self.zone, self.organization_id, total_distance, item_type)
        expected_price = self.base_price + ((total_distance - self.base_distance) * self.per_km_price)
        self.assertEqual(total_price, expected_price)