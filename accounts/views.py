from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('home')


def product(request):
    return HttpResponse('products')


def customer(request):
    return HttpResponse('customer')
