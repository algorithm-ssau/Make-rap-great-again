from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from .models import Rapper

#from .forms import SubscriberForm
# Create your views here.

def home(request):
    rappers = Rapper.objects.all() 
    return render(request, 'main2/home.html', {"rappers": rappers})