from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from super_types.models import SuperType
from .serializers import SuperSerializer
from .models import Super



@api_view(['GET', 'POST'])
def supers_list(request):
    supers_param = request.query_params.get('type')
    supers = Super.objects.all()

    super_types = SuperType.objects.all()
    custom_response_dictionary = {}



    if supers_param:
        supers = Super.objects.filter(super_type__type=supers_param)
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
    
    
    if request.method == 'GET':
        supers = Super.objects.all()

        for super_type in super_types:
            supers = Super.objects.filter(super_type_id=super_type.id)
            serializer = SuperSerializer(supers, many=True)
            custom_response_dictionary[super_type.type] = serializer.data
        return Response(custom_response_dictionary)

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)