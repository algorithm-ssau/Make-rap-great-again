from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Здесь сделать красиво

def miron(request):
    return render(request, 'rapers/miron.html', locals())