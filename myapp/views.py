from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from myapp.models import *

#REGISTERING USER THROUGH REGISTRATION FORM
def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return HttpResponse("credential are not strong")
    else:
        form = UserCreationForm()
        return render(request, "registration.html", {'form' : form})

#LOGGING WITH THE REGISTERED USER CREDENTIAL
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('products')
        else:
            return HttpResponse("User Not Found")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})

#GIVING ACCESS TO PRODUCT PAGE FOR LOGGED IN USERS
@login_required(login_url = 'login')
def products(request):
    all_products = Product.objects.all()
    return render(request, "products.html", {'records' : all_products})