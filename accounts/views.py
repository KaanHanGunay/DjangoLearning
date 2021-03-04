from django.shortcuts import render


def home(request):
    return render(request, 'accounts/dashboard.html')


def product(request):
    return render(request, 'accounts/products.html')


def customers(request):
    return render(request, 'accounts/customers.html')
