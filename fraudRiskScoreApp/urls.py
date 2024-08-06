from django.urls import path
from .views import get_all_riskscore

urlpatterns = [
    path('riskscore/', get_all_riskscore, name='get_all_transactions'),
]
