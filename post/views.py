from django.contrib.auth.models import User
from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView,FormView
from django.db.models import Q

from .forms import CustomerForm
from .models import NewCustomer

class PostListView(ListView):
    template_name= 'list.html'
    model = NewCustomer
    context_object_name='allcustomers'
    paginate_by = 5

    def get_queryset(self):

        word = self.request.GET.get("word")
        if word:
            return NewCustomer.objects.filter(
            Q(Name__icontains=word)|
            Q(Surname__icontains=word)|
            Q(TC__icontains=word)|
            Q(City__icontains=word)|
            Q(District__icontains=word)|
            Q(Telephone__icontains=word))
        return NewCustomer.objects.all().order_by('-Date')


class PostDetailView(DetailView):
    template_name= 'detail.html'
    model = NewCustomer
    context_object_name='NewCustomer'


class PostCreateView(CreateView):
    template_name='create.html'
    form_class = CustomerForm
    success_url ="/post/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView,self).form_valid(form)

 
class PostDeleteView(DeleteView):
    model = NewCustomer
    template_name='delete.html'
    success_url ="/post/"


class RegisterView(FormView):
    template_name = 'sent.html'
    form_class = CustomerForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()    
        else:
            return render(request, "create.html",{"form":form})

        return render(request, self.template_name, {'form': form})


class PostUpdateView(UpdateView):
    model = NewCustomer
    template_name='update.html'
    success_url ="/post/"

    form_class = CustomerForm

def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostUpdateView,self).form_valid(form)