from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Listing
from .serializer import ListingSerializer

class ListingListCreate(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
