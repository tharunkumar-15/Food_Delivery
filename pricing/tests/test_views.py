from django.test import TestCase, Client
from django.urls import reverse
from pricing.models import Organization, Item, Pricing

class CalculateDeliveryPriceViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_valid_post_request(self):
        org = Organization.objects.create(name='Test Organization')
        item = Item.objects.create(type='perishable', description='Test Item')
        Pricing.objects.create(
            organization=org,
            item=item,
            zone='Test Zone',
            base_distance_in_km=10,
            km_price=1.5,
            fix_price=10
        )
        data = {
            'zone': 'Test Zone',
            'organization_id': org.id,
            'total_distance': 15,
            'item_type': 'perishable'
        }
        response = self.client.post(reverse('delivery_price'), data)
        self.assertEqual(response.status_code, 200)

        # Convert total_price to float if it exists
        response_data = response.json()
        total_price = response_data.get('total_price')
        if total_price is not None:
            total_price = float(total_price)
            response_data['total_price'] = total_price

        self.assertDictEqual(response_data, {'total_price': 17.5})

    def test_invalid_post_request(self):
        response = self.client.get(reverse('delivery_price'))
        self.assertEqual(response.status_code, 405)

    def test_pricing_not_found(self):
        data = {
            'zone': 'Non-existent Zone',
            'organization_id': 999,
            'total_distance': 20,
            'item_type': 'perishable'
        }
        response = self.client.post(reverse('delivery_price'), data)
        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(response.content, {'error': 'Pricing information not found'})
