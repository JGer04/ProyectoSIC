from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index/index.html')

def index2(request):
    return render(request, 'index/index_2.html')