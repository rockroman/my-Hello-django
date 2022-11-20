from django.shortcuts import render, HttpResponse


# Create your views here.
def sayHello(request):
    return HttpResponse("Hello!")