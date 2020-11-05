from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from finder.models import Casino
from finder.serializers import CasinoSerializer

class ListCreateCasinos(generics.ListCreateAPIView):
    queryset = Casino.objects.all()
    serializer_class = CasinoSerializer
