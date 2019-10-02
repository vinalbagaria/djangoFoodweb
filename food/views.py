from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request ,'index.html')


def foodOrder(request):
    return  render(request,'food-order.html')