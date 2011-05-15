# Create your views here.
from django.shortcuts import render_to_response, HttpResponse

def login(request):
    return HttpResponse("Login Page")