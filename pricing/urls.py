from django.urls import path
from .views import calculate_delivery_price
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    path('calculate_delivery_price/', calculate_delivery_price, name='delivery_price'),
    path('api_documentation/', schema_view)
]
