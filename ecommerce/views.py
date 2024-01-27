from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''

    return HttpResponse('Welcome to 6410742735 Wasawat Cheepsamut views!')

def item_view(request, item_id):   

    context_data = {
        "item_id": item_id   
        }
    
    return render(request, 'index.html',context= context_data)

def homepage_view(request):
    '''This function render index page of homepage views'''

    return render(request, 'homepage.html')

def category_view(request):
    '''This function render index page of category views'''

    return render(request, 'category.html')

def product_view(request):
    '''This function render index page of product views'''

    return render(request, 'product.html')

def checkout_view(request):
    '''This function render index page of checkout views'''

    return render(request, 'checkout.html')

def contact_view(request):
    '''This function render index page of contact views'''

    return render(request, 'contact.html')