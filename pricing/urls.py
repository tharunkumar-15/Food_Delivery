from django.urls import path, include
from rest_framework import permissions,routers
from .views import calculate_delivery_price
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

schema_view = get_schema_view(
   openapi.Info(
      title="Food_Delivery",
      default_version='v1',
      description="Food_Delivery_Calculator",
      terms_of_service="https://www.food_delivery.com/policies/terms/",
      contact=openapi.Contact(email="food_delivery@yourdomain.com"),
      license=openapi.License(name="food delivery License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
router = DefaultRouter()
urlpatterns = [
    path('api', include(router.urls)),
    path('calculate_delivery_price/', calculate_delivery_price, name='delivery_price'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
