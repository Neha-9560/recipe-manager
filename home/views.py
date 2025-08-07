from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def home(request):
    peoples = [
        {"name": "Amit singh", "age":14},
        {"name": "Neha singh", "age":20},
        {"name": "Priya singh", "age":18}
    ]
    Vegetables =["Potato","Tomato","Onion","Carrot"]
    return render(request, "home/index.html", context={'page':'Django tutorial 2025',"peoples":peoples,"Vegetables":Vegetables})
def about(request):
    context={'page:':'contact'}
    return render(request, "home/about.html",context)
def contact(request):
    context={'page:':'contact'}
    return render(request, "home/contact.html",context)
def success_page(request):
    return HttpResponse("<h1>Welcome to success page</h1>")
