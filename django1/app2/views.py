from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index_app2.html")


def do1(request):
    return render(request, "do1_app2.html")
                                  
                                  
def do2(request):                 
    return render(request, "do2_app2.html")
                               
                               
def do3(request):              
    return render(request, "do3_app2.html")