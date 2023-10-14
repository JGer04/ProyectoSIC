from django.shortcuts import render

# Create your views here.
def cuenta(request):
    return render(request, 'cuenta/cuenta.html')