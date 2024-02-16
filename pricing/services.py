from decimal import Decimal
from .models import Pricing

class PriceCalculator:
    @staticmethod
    def calculate_total_price(zone, organization_id, total_distance, item_type):
        food_delivery = Pricing.objects.filter(
            organization_id=organization_id,
            zone=zone,
            item__type=item_type,
        ).first()

        if not food_delivery:
            return "No such data present in the database for organization_id={}, zone={}, and item_type={}".format(organization_id, zone, item_type)

        base_price = food_delivery.fix_price
        per_km_price = food_delivery.km_price
        base_distance = food_delivery.base_distance_in_km

        if total_distance <= base_distance:
            total_price = base_price
        else:
            extra_distance = total_distance - base_distance
            total_price = base_price + (extra_distance * per_km_price)

        return total_price
