from django.shortcuts import render

# Create your views here.
# from zqxt import views as zqxt_views

from django.http import HttpResponse
from django.http import  HttpResponseRedirect
from django.urls import reverse

def old_add2_redirect(request,a,b):
    return HttpResponseRedirect(
        reverse('add2',args=(a,b))
    )

def index(request):
    return  render(request, 'home.html')
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))
def add2(requset,a,b):
    c = int(a) + int(b)
    return  HttpResponse(str(c))