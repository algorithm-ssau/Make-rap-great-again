from django.shortcuts import render 
from django.http import HttpResponse 
from django.http import HttpResponseRedirect 
from .models import Season 
from .models import Punch

#from .forms import SubscriberForm 
# Create your views here. 

def home2(request):
    seasons = Season.objects.all() 
    return render(request, 'main2/home2.html',  {"seasons": seasons}) 

def punch(request):
    punchs  = Punch.objects.all()
    return render(request, 'main2/punches.html',  {"punchs": punchs}) 

def season1(request, seasons_id):
    season = Season.objects.get(id_season=seasons_id)
    punchs = Punch.objects.filter(id_season=seasons_id)
    data = {"season": season, "punchs": punchs}
    return render(request, 'main2/season_block.html',  context=data)
     
    