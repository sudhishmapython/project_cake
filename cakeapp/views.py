from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from cakeapp.forms import LoginRegister,Ownerform,Userform

# Create your views here.
def index(request):
    return render(request,'index.html')

def owner_registration(request):
    login_form=LoginRegister()
    owner_form=Ownerform()
    if request.method=='POST':
        login_form=LoginRegister(request.POST)
        owner_form=Ownerform(request.POST)
        if login_form.is_valid() and owner_form.is_valid():
            user=login_form.save(commit=False)
            user.is_owner=True
            user.save()
            owner=owner_form.save(commit=False)
            owner.user=user
            owner.save()
            messages.info(request,'register successfully')
            return redirect('index')
    return render(request,'owner_reg.html',{'login_form':login_form,'owner_form':owner_form})



def user_registration(request):
    login_form=LoginRegister()
    user_form=Userform()
    if request.method=='POST':
        login_form=LoginRegister(request.POST)
        user_form=Userform(request.POST)
        if login_form.is_valid() and user_form.is_valid():
            user=login_form.save(commit=False)
            user.is_user=True
            user.save()
            user1=user_form.save(commit=False)
            user1.user=user
            user1.save()
            messages.info(request,'register successfully')
            return redirect('index')
    return render(request,'user_reg.html',{'login_form':login_form,'user_form':user_form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            login(request, user)
            if user.is_staff:
                return redirect('admin_page')
            elif user.is_owner:
                return redirect('supplier_page')

            elif user.is_user:
                return redirect('user_page')
        else:
            messages.error(request, 'INVALID CREDENTIALS')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

