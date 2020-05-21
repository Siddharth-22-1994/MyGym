from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'About.html')