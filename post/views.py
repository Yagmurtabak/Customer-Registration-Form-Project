
from django import forms
from django.core import paginator
from django.shortcuts import render,HttpResponseRedirect
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
        ).distinct()    
    else:
        customers_list = NewCustomer.objects.all()

    paginator = Paginator(customers_list,5)
    page = request.GET.get('page')
    allcustomers = paginator.get_page(page)
    
    return render(request, "list.html",{"allcustomers": allcustomers})


def postdetail_view(request,id):
    yazıNesne = NewCustomer.objects.get(id=id)
    return render(request, "detail.html",{ "NewCustomer": yazıNesne})

def postcreate_view(request):
    form = CustomerForm()
    return render(request, "create.html", {"form": form})

def formdoldur_view(request):
    form = CustomerForm(request.GET)
    if form.is_valid():
        form.save()
        
        return render(request, "sent.html")
    

def postupdate_view(request,id):
    if request.GET.get("isim"):
        isim  = request.GET.get("isim")
        soyisim = request.GET.get("soyisim")
        kimlikno = request.GET.get("kimlikno")
        sehir = request.GET.get("sehir")
        ilce = request.GET.get("ilce")
        numara = request.GET.get("numara")
        id = request.GET.get("id")

        yazıNesne = NewCustomer.objects.get(id=id)

        yazıNesne.Name  = isim
        yazıNesne.Surname = soyisim
        yazıNesne.TC = kimlikno
        yazıNesne.City = sehir
        yazıNesne.District = ilce
        yazıNesne.Telephone = numara
        yazıNesne.save()
    else:
        yazıNesne = NewCustomer.objects.get(id=id)   
        
    return render(request, "update.html", {"NewCustomer":yazıNesne})

def postdelete_view(request, id):
    yazıNesne = NewCustomer.objects.get(id=id)
    yazıNesne.delete()
    
    return HttpResponseRedirect("/post")