from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView , DetailView
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.contrib.auth import authenticate, login, logout 
from .forms import *
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy ,reverse
from django.contrib import messages




class Login_View(View):

    

    def get(self, request):
        form = Login_Forms()
        return render(request, "registration/login.html", {"form":form})
    
    
    def post(self, request):
        form = Login_Forms(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect("core:home")
        else:
            return render(request, "registration/login.html", {"form":form})
            


class Signup_View(View):
    
    def get(self, request):
        form = Signup_Form()
        return render(request, 'registration/signup.html', {"form":form})
    

    def post(self, request):
        form = Signup_Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            password = form.cleaned_data["password1"]


            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            CustomerProfile.objects.create(
                user=user,
                phone=phone,
                balance=0,
            )
            return redirect("accounts:login")
        else:
            return render(request, "registration/signup.html", {"form": form})

class Logout_View(View):
    
    def get(self, request):
        logout(request)
        return render(request, "registration/logout.html")
    


class CustomerPanel(View):

    def get(self, request):
        customer = request.user.customerprofile

        return render(request, "registration/customer_panel.html", {"customer":customer})
    

class Payment(View):

    def get(self, request):
        return render(request, "registration/payment.html")

    def post(self, request):
        profile = request.user.customerprofile
        amount = int(request.POST.get("amount"))        

        profile.balance += amount
        profile.save()
        
        return redirect("core:home")