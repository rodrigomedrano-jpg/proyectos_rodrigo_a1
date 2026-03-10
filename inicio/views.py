from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("Saludos, mi nombre es Rodrigo🫡")

def perro(request):
    return HttpResponse("Guau Guau")

def gato(request):
    return HttpResponse("Miau Miau")

