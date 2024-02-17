from django.http import JsonResponse
from .services import PriceCalculator
from django.views.decorators.csrf import csrf_exempt
from .models import Pricing, Organization
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view

@csrf_exempt
@swagger_auto_schema(method='GET', 
    operation_description="Calculate delivery price based on zone, organization, total distance, and item type.",
    manual_parameters=[
        openapi.Parameter('zone', openapi.IN_QUERY, description="Delivery zone", type=openapi.TYPE_STRING),
        openapi.Parameter('organization_id', openapi.IN_QUERY, description="Organization ID", type=openapi.TYPE_INTEGER),
        openapi.Parameter('total_distance', openapi.IN_QUERY, description="Total distance in kilometers", type=openapi.TYPE_INTEGER),
        openapi.Parameter('item_type', openapi.IN_QUERY, description="Type of item (perishable or non-perishable)", type=openapi.TYPE_STRING),
    ],
    responses={200: openapi.Response('Successful response', schema=openapi.Schema(type="object", properties={'total_price': openapi.Schema(type="number", description="Total price")})),
        400: openapi.Response('Bad Request', schema=openapi.Schema(type="object", properties={'error': openapi.Schema(type="string", description="Error message")})),
        404: openapi.Response('Not Found', schema=openapi.Schema(type="object", properties={'error': openapi.Schema(type="string", description="Error message")}))
    })
@api_view(['GET'])
def calculate_delivery_price(request):
    if request.method == 'GET':
        zone = request.GET.get('zone')
        organization_id = request.GET.get('organization_id')
        total_distance_str = request.GET.get('total_distance')
        item_type = request.GET.get('item_type')
        
        if not (zone and organization_id and total_distance_str and item_type):
            missing_params = []
            if not zone:
                missing_params.append('zone')
            if not organization_id:
                missing_params.append('organization_id')
            if not total_distance_str:
                missing_params.append('total_distance')
            if not item_type:
                missing_params.append('item_type')
            return JsonResponse({'error': f'Required parameters are missing: {", ".join(missing_params)}.'}, status=400)

        try:
            total_distance = int(total_distance_str)
        except ValueError:
            return JsonResponse({'error': 'Invalid value for total_distance. Please provide a valid integer value.'}, status=400)

        try:
            organization = Organization.objects.get(pk=organization_id)
            pricings = Pricing.objects.filter(zone=zone, organization_id=organization_id, item__type=item_type)
            if pricings.exists():
                pricing = pricings.first()
            else:
                raise Pricing.DoesNotExist
        except Organization.DoesNotExist:
            return JsonResponse({'error': 'Organization not found'}, status=404)
        except Pricing.DoesNotExist:
            return JsonResponse({'error': 'Pricing information for the specified organization and item type not found'}, status=404)


        total_price = PriceCalculator.calculate_total_price(zone, organization.id, total_distance, item_type)
        
        if total_price is None:
            return JsonResponse({'error': 'Pricing information not found'}, status=404)
        
        formatted_price = round(total_price, 1)
        return JsonResponse({'total_price': formatted_price})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)
