from django.contrib import admin
from django.urls import path
from .views import *


app_name = "accounts"


urlpatterns = [
    path('login/' ,Login_View.as_view(),name="login"),
    path('signup/', Signup_View.as_view() , name="signup"),
    path('logout/' ,Logout_View.as_view(), name="logout"),
    path('customer_panel/', CustomerPanel.as_view(),name="customer_panel"),
    path('balance/',Payment.as_view(),name="payment")
]
