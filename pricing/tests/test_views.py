# tests.py
from django.test import TestCase, Client
from django.urls import reverse
from pricing.models import Pricing, Organization, Item
import json

class CalculateDeliveryPriceTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.organization = Organization.objects.create(name="Test Org")
        self.item = Item.objects.create(type="perishable", description="Test Item")
        Pricing.objects.create(
            organization=self.organization,
            item=self.item,
            zone="A",
            base_distance_in_km=100,
            km_price=5.0,
            fix_price=10.0
        )

    def test_successful_calculation(self):
        url = reverse('delivery_price')
        data = {'zone': 'A', 'organization_id': self.organization.id, 'total_distance': '100', 'item_type': 'perishable'}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('total_price', response.json())

    def test_missing_parameters(self):
        url = reverse('delivery_price')
        data = {'zone': 'A'}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    def test_invalid_total_distance(self):
        url = reverse('delivery_price')
        data = {'zone': 'A', 'organization_id': self.organization.id, 'total_distance': 'abc', 'item_type': 'perishable'}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    def test_non_existing_organization(self):
        url = reverse('delivery_price')
        data = {'zone': 'A', 'organization_id': 999, 'total_distance': '100', 'item_type': 'perishable'}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.json())

    def test_non_existing_pricing_information(self):
        url = reverse('delivery_price')
        data = {'zone': 'X', 'organization_id': self.organization.id, 'total_distance': '100', 'item_type': 'perishable'}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.json())
