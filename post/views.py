
from django import forms
from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import CustomerForm
from .models import NewCustomer
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def postlist_view(request):
    word = request.GET.get("word")
    if word:
        customers_list=NewCustomer.objects.filter(
            Q(Name__icontains=word)|
            Q(Surname__icontains=word)|
            Q(TC__icontains=word)|
            Q(City__icontains=word)|
            Q(District__icontains=word)|
            Q(Telephone__icontains=word)
        ).distinct().order_by('-Date')    
    else:
        customers_list = NewCustomer.objects.all().order_by('-Date')

    paginator = Paginator(customers_list,5)
    page = request.GET.get('page')
    allcustomers = paginator.get_page(page)
    
    return render(request, "list.html",{"allcustomers": allcustomers})


def postdetail_view(request,id):
    NewCustomerObject = NewCustomer.objects.get(id=id)
    return render(request, "detail.html",{ "NewCustomer": NewCustomerObject})

def postcreate_view(request):
    form = CustomerForm()
    return render(request, "create.html", {"form": form})

def newform_view(request):
        
        if request.method == "POST" :
            form = CustomerForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, "sent.html" ,{"CustomerForm":CustomerForm})
            if not() :
                return render(request, "error.html",{"CustomerForm":CustomerForm})     
            

 
        

def postupdate_view(request,id):
        if request.POST.get("name"):
            name  = request.POST.get("name")
            surname = request.POST.get("surname")
            identificationnumber = request.POST.get("identificationnumber")
            city = request.POST.get("city")
            district = request.POST.get("district")
            telephone = request.POST.get("telephone")
            id = request.POST.get("id")

            NewCustomerObject = NewCustomer.objects.get(id=id)

            NewCustomerObject.Name  = name
            NewCustomerObject.Surname = surname
            NewCustomerObject.TC = identificationnumber
            NewCustomerObject.City = city
            NewCustomerObject.District = district
            NewCustomerObject.Telephone = telephone
            NewCustomerObject.save()
        else:
            NewCustomerObject = NewCustomer.objects.get(id=id)   
        
        return render(request, "update.html", {"NewCustomer":NewCustomerObject})



def postdelete_view(request, id):
    NewCustomerObject = NewCustomer.objects.get(id=id)
    NewCustomerObject.delete()
    
    return HttpResponseRedirect("/post")


