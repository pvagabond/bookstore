from django.shortcuts import render

def index(req):
    #req is the http obj, that contains all the metadata
    return render(req, 'template.html')

def store(req):
    return render(req, 'store.html')
