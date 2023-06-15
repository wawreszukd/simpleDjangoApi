from django.urls import path
from .views import *
urlpatterns = [
    path('all/',getAllDrinks, name='getAll'),
    path('add/',addDrink, name='addDrink'),
    path('get/<int:getId>',getOneDrink, name='getOne'),
    path('delete/<int:getId>',deleteDrink, name='delete')
]