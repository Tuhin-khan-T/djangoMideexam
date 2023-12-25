from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Car, Brand

class CarListView(ListView):
    model = Car
    template_name = 'carapp/car_list.html'  # Corrected typo

class CarDetailView(DetailView):
    model = Car
    template_name = 'carapp/car_detail.html'  # Corrected typo
