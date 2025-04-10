from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    category=categorie.objects.all()
    context={
        'category':category
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')

def loml(request):
    return render(request, 'loml.html')

def articless(request):
    articles = article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articless.html', context)