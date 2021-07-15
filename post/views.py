from django.shortcuts import render

# Create your views here.

def home_view(request):
    page = "Home Page"

    return render(request, "page.html", {"page": page})


def Customers_view(request):
    page = "Customers"
    return render(request, "page.html", {"page": page})

def NewRegistration_view(request):
    page = "New Registration"
    return render(request, "page.html", {"page": page})