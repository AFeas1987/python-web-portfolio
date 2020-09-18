from django.shortcuts import render
from django.http import HttpResponse

def resume(request):
    return render(request, "resume.html")

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")