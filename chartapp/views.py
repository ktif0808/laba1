from django.shortcuts import render, redirect
from . models import Product
from . forms import ProductForm
from django.http import HttpResponse
# Create your views here.
from django.http import JsonResponse
from django.utils import timezone
from datetime import date
import subprocess

def add(request, article_id):

    context = {}
    ip = ""
    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    ip = abs(hash(ip)) % (10 ** 6)
    a = Product(category="UserID " + str(ip), num_of_products=int(article_id))
    a.save()

    today = date.today()
    timVar = today.strftime("%d.%m.%Y")
    return JsonResponse({'Status': "OK",'UserID': str(ip), 'Value': str(article_id), 'Time' : str(timVar)})


def index(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm() 
        
    resultJava = subprocess.run(['java', '-version'], capture_output=True, text=True)
    java_version = resultJava.stderr
    context = {
        "products": products,
        "form": form,
        "java_version": java_version
    }

    return render(request, 'chartapp/index.html', context)


def getUsers(request):
    queryset = Product.objects.all()
    return JsonResponse({"users" : list(queryset.values())})
