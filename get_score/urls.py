from django.urls import path
from .views import get_score

urlpatterns = [
    path('', get_score)
]
