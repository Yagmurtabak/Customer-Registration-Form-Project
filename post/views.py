
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import yazı

# Create your views here.

def postlist_view(request):
    allcustomers = yazı.objects.all()
    return render(request, "list.html",{"allcustomers": allcustomers})

def postdetail_view(request,id):
    yazıNesne = yazı.objects.get(id=id)
    return render(request, "detail.html",{ "yazı": yazıNesne})

def postcreate_view(request):
    page = "NewRegistration"
    return render(request, "create.html", {"page": page})

def formdoldur_view(request):
    isim = request.GET.get("isim")
    soyisim = request.GET.get("soyisim")
    kimlikno = request.GET.get("kimlikno")
    sehir = request.GET.get("sehir")
    ilce = request.GET.get("ilce")
    numara = request.GET.get("numara")

    yazı.objects.create(isim=isim, soyisim=soyisim, kimlikno=kimlikno, sehir=sehir, ilce=ilce, numara=numara)
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