from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'static/home.html')

def about(request):
    return render(request, 'static/about.html')
