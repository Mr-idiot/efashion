from django.shortcuts import render
from .models import Shirt

def index(request):
    return render(request,'shopping/index.html',{})
def garments(request):
    garments = Shirt.objects.all()
    return render(request,'shopping/garments.html',{'garments':garments})
