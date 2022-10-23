from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import RecordSerializer

# Create your views here.
@api_view(["POST"])
def get_score(request, *args, **kwargs):
    instance=request.data
    serializer = RecordSerializer(data=instance)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    return Response({}, status=400)
