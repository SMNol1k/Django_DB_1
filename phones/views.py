# views.py
from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    phones = Phone.objects.all()
    context = {'phones': phones}
    sort_by = request.GET.get('sort')
    if sort_by == 'name':
        phones = phones.order_by('name')
    elif sort_by == 'price_asc':
        phones = phones.order_by('price')
    elif sort_by == 'price_desc':
        phones = phones.order_by('-price')
    return render(request, 'catalog.html', context)

def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)