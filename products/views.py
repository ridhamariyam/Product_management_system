from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt

@login_required
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products_detail.html', {'product': product})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'product_form.html', context)

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, 'product_form.html', context)

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    context = {'product': product}
    return render(request, 'product_confirm_delete.html', context)


@csrf_exempt
@require_GET
def product_data(request):
    product_ids = request.GET.getlist('product_ids')
    name_contains = request.GET.get('name_contains')

    products = Product.objects.all()

    if product_ids:
        products = products.filter(id__in=product_ids)

    if name_contains:
        products = products.filter(name__icontains=name_contains)

    data = {
        'products': list(products.values('id', 'name', 'description', 'price'))
    }
    return JsonResponse(data)