from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from . models import Locations
from . models import Product
from .forms import Location_New_Account_Form
from .forms import Location_New_Product_Form


def dashboard(request):
    return render(request, 'cms/dashboard.html')


def contests(request):
	return render_to_response('cms/contests.html', {'title': 'Contests'}, context_instance=RequestContext(request))
    # return render(request, 'cms/contests.html')


def promos(request):
    return render(request, 'cms/promos.html')


def newsfeeds(request):
    return render(request, 'cms/newsfeeds.html')


def location_accounts(request):
    # return render(request, 'cms/location_accounts.html')
    accounts = Locations.objects.all().order_by('-timestamp')
    return render(request, 'cms/location_accounts.html', {'accounts': accounts})


def location_del_account(request, pk):
    account = get_object_or_404(Locations, pk=pk)
    account.delete()
    accounts = Locations.objects.all().order_by('-timestamp')
    return render(request, 'cms/location_accounts.html', {'accounts': accounts})


# @login_required
def location_new_account(request):
    if request.method == 'POST':
        form = Location_New_Account_Form(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            # account.author = request.user
            # account.published_date = timezone.now()
            account.save()
            # return redirect('cms.views.location_new_account', pk = post.pk)
            # accounts = Locations.objects.all().order_by('-timestamp')
            # return render(request, 'cms/location_accounts.html', {'accounts': accounts})
    else:
        form = Location_New_Account_Form()
    return render(request , 'cms/location_new_account.html', {'form': form})
    # return render(request, 'cms/location_new_account.html')
    # accounts = Locations.objects.all().order_by('-timestamp')
    # return render(request, 'cms/location_accounts.html', {'accounts': accounts})

def location_edit_account(request, pk):
    account = get_object_or_404(Locations, pk=pk)
    if request.method == 'POST':
        form = Location_New_Account_Form(request.POST, instance=account)
        if form.is_valid():
            account = form.save(commit=False)
            # account.author = request.user
            # account.published_date = timezone.now()
            account.save()
            # return redirect('cms.views.location_new_account', pk = post.pk)
            accounts = Locations.objects.all().order_by('-timestamp')
            # return render(request, 'cms/location_accounts.html', {'accounts': accounts, 'mode': 'edited'})
            return render(request , 'cms/location_new_account.html', {'form': form, 'mode': 'edited'})
    else:
        form = Location_New_Account_Form(instance=account)
    return render(request , 'cms/location_new_account.html', {'form': form})


def location_del_account(request, pk):
    account = get_object_or_404(Locations, pk=pk)
    account.delete()
    accounts = Locations.objects.all().order_by('-timestamp')
    return render(request, 'cms/location_accounts.html', {'accounts': accounts})

def location_products(request):
    # return render(request, 'cms/location_products.html')
    products = Product.objects.all().order_by('-timestamp')
    return render(request, 'cms/location_products.html', {'products': products})


# @login_required
def location_new_product(request):
    if request.method == 'POST':
        form = Location_New_Product_Form(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
    else:
        form = Location_New_Product_Form()
    return render(request , 'cms/location_new_product.html', {'form': form})


# @login_required
def location_del_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    products = Product.objects.all().order_by('-timestamp')
    return render(request, 'cms/location_prouducts.html', {'products': products})


# @login_required
def location_edit_product(request):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = Location_New_Product_Form(request.POST, instance=product)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
    else:
        form = Location_New_Product_Form(instance=product)
    return render(request , 'cms/location_new_product.html', {'form': form})


def location_promotions(request):
    return render(request, 'cms/location_promotions.html')

def rewards(request):
    return render(request, 'cms/rewards.html')