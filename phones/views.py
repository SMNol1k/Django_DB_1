from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    phones = Phone.objects.all()
    context = {'phones': phones}
    sort_by = request.GET.get('sort')
    if sort_by == 'name':
        context['phones'] = phones.order_by('name')
    elif sort_by == 'price_asc':
        context['phones'] = phones.order_by('price')
    elif sort_by == 'price_desc':
        context['phones'] = phones.order_by('-price')
    return render(request, 'catalog.html', context)

def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, 'product.html', context)