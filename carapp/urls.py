

from django.urls import path
from .views import CarListView, CarDetailView

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car_list'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
]
