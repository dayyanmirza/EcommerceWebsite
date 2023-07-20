from django.shortcuts import render

# Create your views here. View functions/ methods take a web (http) request and return a web (http)response.

def store(request): # takes request object as a parameter 
    context = {} # context is an empty python dictionary --> used to hold data that will be passed to the html template for rendering.
    return render(request, 'store/store.html', context) # renders the html template store.html and passes the context dictionary to it. The render template is provided by django and is used to combine the template with the data in the context dictionary.

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context) 

"""
Example:

When a user makes a request to view the cart page.
Django will call the cart function. Inside the function you can perform various operations related to the car, i.e. caluclate prices, fetches items.
After data processing the data that you want to display on the html page will be stored in the context dictionary.
Once the data is prepared the render function is called with the following parameters request - incoming http request object, store/cart.html - path to the html template that's rendered, and context - dictionary containing the data that will be passed to the template. 
"""

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
    