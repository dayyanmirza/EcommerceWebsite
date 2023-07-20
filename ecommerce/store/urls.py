from django.urls import path
from . import views 
############### Continue project from step 3 on this page: https://codewithsteps.herokuapp.com/part/087c411f-a487-4ce1-ab6f-ae2016273e27/ Base URLs Configuration
urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout")
]