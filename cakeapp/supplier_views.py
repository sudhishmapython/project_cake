from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required(login_url='login_view')
def supplier_page(request):
    return render(request, 'supplier_temp/home.html')
