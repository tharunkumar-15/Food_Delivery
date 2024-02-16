from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pricing.views import API

class TestUrls(SimpleTestCase):
    def test_calculate_delivery_price_resolved(self):
        url = reverse('delivery_price')
        resolved_func = resolve(url).func
        api_instance = API()
        self.assertEquals(resolved_func, api_instance.calculate_delivery_price)
