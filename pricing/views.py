from django.http import JsonResponse
from .services import PriceCalculator
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def calculate_delivery_price(request):
    if request.method == 'GET':
        # Retrieving data from query parameters instead of POST data
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
            total_distance = int(total_distance_str)  # Convert total_distance to integer
        except ValueError:
            return JsonResponse({'error': 'Invalid value for total_distance. Please provide a valid integer value.'}, status=400)

        total_price = PriceCalculator.calculate_total_price(zone, organization_id, total_distance, item_type)
        print("total_price:", total_price)
        
        if isinstance(total_price, str):
            return JsonResponse({'error': total_price}, status=404)
        
        formatted_price = round(total_price, 1)
        return JsonResponse({'total_price': formatted_price})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)
