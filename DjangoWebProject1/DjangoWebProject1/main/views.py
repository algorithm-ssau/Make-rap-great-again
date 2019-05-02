from django.shortcuts import render
from django.http import HttpResponse
#from .forms import SubscriberForm
# Create your views here.

def home(request):
    return render(request, 'main/home.html', locals())