from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pricing.views import calculate_delivery_price

class TestUrls(SimpleTestCase):
    def test_calculate_delivery_price_resolved(self):
        url = reverse('delivery_price')
        resolved_func = resolve(url).func
        self.assertEquals(resolved_func,calculate_delivery_price)
