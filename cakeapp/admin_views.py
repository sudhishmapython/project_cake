from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from cakeapp.forms import CategoryForm,CakeForm
from cakeapp.models import Cake,Category


@login_required(login_url='login_view')
def admin_page(request):
    return render(request, 'admin_temp/home.html')


@login_required(login_url='login_view')
def add_catogory(request):
    form=CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Category Added Successfully')
            return redirect('add_catogory')
    return render(request,'admin_temp/add_category.html',{'form':form})


@login_required(login_url='login_view')
def cat_view(request):
    category = Category.objects.all()
    return render(request,'admin_temp/view_category.html', {'form': category})


@login_required(login_url='login_view')
def cat_update(request,id):
    n = Category.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            return redirect('cat_view')
    else:
        form = CategoryForm(instance=n)
    return render(request, 'admin_temp/category_update.html', {'form': form})


@login_required(login_url='login_view')
def cat_delete(request, id):
    n = Category.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, 'Category Deleted Successfully')
        return redirect('cat_view')
    else:
        return redirect('cat_view')



@login_required(login_url='login_view')
def cake_add(request):
    form=CakeForm()
    if request.method == 'POST':
        form = CakeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Cake Added Successfully')
            return redirect('cake_add')
    return render(request,'admin_temp/add_cake.html',{'form':form})


@login_required(login_url='login_view')
def cake_view(request):
    cakes = Cake.objects.all()
    return render(request,'admin_temp/view_cake.html', {'form': cakes})



@login_required(login_url='login_view')
def cake_update(request,id):
    n = Cake.objects.get(id=id)
    if request.method == 'POST':
        form = CakeForm(request.POST or None, request.FILES, instance=n)
        if form.is_valid():
            form.save()
            return redirect('cake_view')
    else:
        form = CakeForm(instance=n)
    return render(request, 'admin_temp/cake_update.html', {'form': form})


@login_required(login_url='login_view')
def cake_delete(request, id):
    n = Cake.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, 'Cake Deleted Successfully')
        return redirect('cake_view')
    else:
        return redirect('cake_view')

