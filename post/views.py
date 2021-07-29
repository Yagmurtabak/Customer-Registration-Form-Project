from django.shortcuts import  redirect, render,HttpResponseRedirect
from django.db.models import Q
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView

from .forms import CustomerForm
from .models import NewCustomer


class PostListView(ListView):
    template_name= 'list.html'
    model = NewCustomer
    context_object_name='allcustomers'
    paginate_by = 5
    ordering = ['-Date']

    
class PostDetailView(DetailView):
    template_name= 'detail.html'
    model = NewCustomer
    context_object_name='NewCustomer'


class PostCreateView(CreateView):
    def get(self,request,*args,**kwargs):
        form = CustomerForm()
        return render(request, "create.html", {"form": form})

 
class PostDeleteView(DeleteView):
    model = NewCustomer
    template_name='delete.html'
    success_url ="/post/"


def newform_view(request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()    
            return render(request, "sent.html")
        else:
            return render(request, "create.html",{"form":form})

class PostUpdateViev(UpdateView):
    model = NewCustomer
    template_name='update.html'
    success_url ="/post/"

    form_class = CustomerForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostUpdateViev,self).form_valid(form)

