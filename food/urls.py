from django.contrib import admin
from django.urls import path,include
from food import views as food_views


urlpatterns = [
    path('', food_views.index ,name = "index"),
    path('food-order/', food_views.foodOrder , name = "food-order")
]
