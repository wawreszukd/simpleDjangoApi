from django.shortcuts import render, HttpResponse, redirect, Http404
from django.http import JsonResponse
from .models import *
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def getAllDrinks(request):
    if request.method == 'GET':

        return render(request, 'allDrinks.html', {'title': 'All items', 'drinks': Drink.objects.all(), 'authcheck': request.user.is_authenticated})
    else:
        return Http404()
@login_required(login_url='login')
def addDrink(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        drink = Drink.objects.create(name=name, description=request.POST.get('description'))
        drink.save()
        return redirect('getAll')
    if request.method == 'GET':
        return render(request,'addDrinks.html',{'title': 'Add an item' , 'authcheck': request.user.is_authenticated})
@login_required(login_url='login')
def getOneDrink(request, getId):
    if request.method == 'GET':
        drink = Drink.objects.get(id=getId)
        return JsonResponse({'name': drink.name, 'description': drink.description})
    return Http404()
@login_required(login_url='login')
def deleteDrink(request, getId):
    if request.method == 'GET':
        drink = Drink.objects.get(id=getId)
        drink.delete()
        return redirect('getAll')
    else:
        return Http404()