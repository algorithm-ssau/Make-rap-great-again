from django.shortcuts import render 
from django.http import HttpResponse 
from django.http import HttpResponseRedirect 
from .models import Season 

#from .forms import SubscriberForm 
# Create your views here. 

def home2(request):
    seasons = Season.objects.all() 
    return render(request, 'main2/home2.html',  {"seasons": seasons}) 

def season1(request, seasons_id):
    seasons = Season.objects.all() 
    return render(request, 'main2/home2.html',  {"seasons": seasons}) 