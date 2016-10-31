from django.shortcuts import render

from .models import Book 

def index(req):
    #req is the http obj, that contains all the metadata
    return render(req, 'template.html')

def store(req):
    count = Book.objects.all().count()
    context = { 'count' : count }
    return render(req, 'store.html', context)
