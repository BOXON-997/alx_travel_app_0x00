# listings/urls.py

from django.urls import path
from .views import ListingListCreate

urlpatterns = [
    path("", ListingListCreate.as_view(), name="listings"),
]
