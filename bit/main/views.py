from django.shortcuts import render

# Create your views here.

def mainp(request):
    return render(request, 'main.html')