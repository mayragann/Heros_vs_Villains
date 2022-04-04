from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperTypeSerializer
from super_types.models import SuperType

@api_view(['GET'])
def supers_type_list(request):
    
    if request.method == 'GET':
        supers_type = SuperType.objects.all()
        serializer = SuperTypeSerializer(supers_type, many=True)
        return Response(serializer.data)