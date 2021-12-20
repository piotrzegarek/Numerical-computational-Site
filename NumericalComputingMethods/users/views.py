from django.shortcuts import render, HttpResponse

# Create your views here.
def users(request):
    return HttpResponse('<h1> im from users </h1>')