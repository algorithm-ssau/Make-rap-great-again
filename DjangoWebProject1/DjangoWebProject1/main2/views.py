from django.shortcuts import render
from django.http import HttpResponse
#from .forms import SubscriberForm
# Create your views here.

def home2(request):
    return render(request, 'main2/home2.html', locals())