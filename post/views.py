
from django import forms
from django.core import paginator
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import yazı
from .forms import CreateForms
from django.core.paginator import EmptyPage, Page,PageNotAnInteger,Paginator
from django.db.models import Q

# Create your views here.

def postlist_view(request):
    word = request.GET.get("word")
    if word:
        customers_list=yazı.objects.filter(
            Q(Name__contains=word),
            Q(Surname__contains=word),
            Q(TC__contains=word),
            Q(City__contains=word),
            Q(District__contains=word),
            Q(Telephone__contains=word)
        ).distinct()
    else:
        customers_list = yazı.objects.all()    
    paginator = Paginator(customers_list,5)

    page = request.GET.get('page')
    allcustomers = paginator.get_page(page)

    return render(request, "list.html",{"allcustomers": allcustomers})


def postdetail_view(request,id):
    yazıNesne = yazı.objects.get(id=id)
    return render(request, "detail.html",{ "yazı": yazıNesne})

def postcreate_view(request):
    form = CreateForms()
    return render(request, "create.html", {"form": form})

def formdoldur_view(request):
    form = CreateForms(request.GET)
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

        yazıNesne = yazı.objects.get(id=id)

        yazıNesne.Name  = isim
        yazıNesne.Surname = soyisim
        yazıNesne.TC = kimlikno
        yazıNesne.City = sehir
        yazıNesne.District = ilce
        yazıNesne.Telephone = numara
        yazıNesne.save()
    else:
        yazıNesne = yazı.objects.get(id=id)   
        
    return render(request, "update.html", {"yazı":yazıNesne})

def postdelete_view(request, id):
    yazıNesne = yazı.objects.get(id=id)
    yazıNesne.delete()
    
    return HttpResponseRedirect("/post")