from django.shortcuts import render
from .models import VineItem
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['POST'])
def create_db(request):
    VineItem.objects.all().delete()
    bulc=[]
    for item in request.data:
        bulc.append(VineItem(
        item['index'],
        item['inStock'],
        item['price'][1:],
        item['picture'],
        item['year'],
        item['color'],
        item['type'],
        item['city'],
        item['name'],
        item['company'],
        item['about'],
        item['tags'][0]))

    VineItem.objects.bulk_create(bulc)
    
    return Response('OK',status=201)