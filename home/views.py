from django.shortcuts import render

# Create your views here.

def home_view(request):
    page = "Home Page"

    return render(request, "page.html", {"page": page})