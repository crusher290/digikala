from typing import Any

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *

class Login_Forms(forms.Form):
    
    username = forms.CharField(label="",widget=forms.TextInput(attrs={"placeholder":"Username"}), error_messages={"required":"Username is required."})
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={"placeholder":"Password"}), error_messages={"required":"Password is required"})

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password.")
        
        return cleaned_data

class Signup_Form(forms.Form):

    username = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder":"Username"}),required=False)
    email = forms.EmailField(label="",widget=forms.EmailInput(attrs={"placeholder":"Email"}),required=False)
    phone = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder":"Phone Number"}),required=False)
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder":"Password"}),required=False)
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}),required=False)
    

    


    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            self.add_error("username", "Username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            self.add_error("email", "Email already exists.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if CustomerProfile.objects.filter(phone=phone).exists():
            self.add_error("phone", "this phone number is already exists.")
        return phone

    def clean(self):
        cleaned_data = super().clean()

        for field in ["username", "email", "phone", "password1", "password2"]:
            if not cleaned_data.get(field):
                self.add_error(field, "This field is required.")
        
        return cleaned_data
    
    

    


