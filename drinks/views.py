from django.core.serializers import serialize
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def drink_list(request):

    if request.method == 'GET':
        #get the drinks
        drinks = Drink.objects.all()
        # serialize them
        serializer = DrinkSerializer(drinks, many=True)
        # return the json to user
        return JsonResponse({'drinks':serializer.data}, safe=False)

    if request.method == 'POST':
        # get data from user input
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        
@api_view(['GET','PUT','DELETE']) #'PUT' id for editing
def drink_detail(request, id):

    # create th drink object once
    try:
       drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        pass


