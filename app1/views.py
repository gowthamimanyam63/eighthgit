from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def string1(request):
    return HttpResponse('<h3>This is belongs to string1</h3>')

def string2(request):
    return HttpResponse('<h2><i>This is belongs to string2</i></h2>')