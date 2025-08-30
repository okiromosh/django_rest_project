from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def drink_list(request):
    #get the drinks
    drinks = Drink.objects.all()
    # serialize them
    serializer = DrinkSerializer(drinks, many=True)
    # return the json to user
    return JsonResponse({'drinks':serializer.data}, safe=False)
