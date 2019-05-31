from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from .models import Rapper

#from .forms import SubscriberForm
# Create your views here.

def home(request):
    rappers = Rapper.objects.all() 
    return render(request, 'main/home.html', {"rappers": rappers})

def rapper(request):
    #rappers = Rapper.objects.all() 
    #return render(request, 'main/home3.html', {"rappers": rappers})
    rapper = Rapper.objects.get(id_rapper=1)
    return render(request, 'main/rapper_block.html', {"rapper": rapper})

def rapper1(request, rapper_id):
    rapper = Rapper.objects.get(id_rapper=rapper_id)
    return render(request, 'main/rapper_block.html', {"rapper": rapper})