from django.shortcuts import render
from django.http import HttpResponse


def index(request):
   # return HttpResponse("YO")
    return render(request,'projectx/index.html')        
