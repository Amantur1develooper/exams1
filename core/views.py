from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator

def main(request):
    search = request.GET.get('search',False)
    if search:
        product = Product.objects.filter(title__icontains=search)
    else:
        product = Product.objects.all()
    category = Category.objects.all()
    paginator = Paginator(product, 1)
    page = int(request.GET.get('page', 1))
    product = paginator.get_page(page)
    return render(request,'index.html', {'product':product,'category':category})


def detail(request, id):
    product = get_object_or_404(Product, id=id)
    category = Category.objects.all()
    return render(request, 'detail.html', {'product':product,'category':category,})

def category(request,pk):
    product = Product.objects.filter(category=pk)
    category_name = Category.objects.get(id=pk).name
    category = Category.objects.all()
    return render(request, 'index.html', {'product':product, 'category':category,'category_name':category_name})

