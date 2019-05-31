from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from .models import Rapper
from .models import Punch

#from .forms import SubscriberForm
# Create your views here.

def home(request):
    rappers = Rapper.objects.all() 
    return render(request, 'main/home.html', {"rappers": rappers})

def rapper1(request, rapper_id):
    rapper = Rapper.objects.get(id_rapper=rapper_id)
    punchs = Punch.objects.filter(id_rapper=rapper_id)
    data = {"rapper": rapper, "punchs": punchs}
    return render(request, 'main/rapper_block.html',  context=data)