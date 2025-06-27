from django.shortcuts import render
from django.http import HttpResponse
def home(request):
       return HttpResponse('<h1 align="center" >hello Django0!</h1>')
def mca101(request):
       return HttpResponse('<h1 align="center">Discreate mathematics</h1>')
def mca102(request):
       return HttpResponse('<h1 align="center">Java</h1>')
def mca103(request):
       return HttpResponse('<h1 align="center">Computer Organization</h1>')
def mca104(request):
       return HttpResponse('<h1 align="center">Operating System</h1>')
def mca105(request):
       return HttpResponse('<h1 align="center">Accounting</h1>')



