from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def season1(request):
    return render(request, 'seasons/season1.html', locals())