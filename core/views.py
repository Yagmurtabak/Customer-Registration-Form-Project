from django.contrib import auth
from django.contrib.auth import forms
from django.shortcuts import redirect, render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView,FormView
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

from .forms import CustomerForm
from .models import NewCustomer


class customerListView(ListView):
    template_name= 'list.html'
    model = NewCustomer
    context_object_name='allcustomers'
    paginate_by = 5

    def get_queryset(self):

        word = self.request.GET.get("word")
        if word:
            return NewCustomer.objects.filter(
            Q(name__icontains=word)|
            Q(surname__icontains=word)|
            Q(tc__icontains=word)|
            Q(city__icontains=word)|
            Q(district__icontains=word)|
            Q(telephone__icontains=word))
        return NewCustomer.objects.all().order_by('-date')


class customerDetailView(DetailView):
    template_name= 'detail.html'
    model = NewCustomer
    context_object_name='NewCustomer'


class customerCreateView(CreateView):
    template_name='create.html'
    form_class = CustomerForm
    success_url ="/core/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(customerCreateView,self).form_valid(form)

 
class customerDeleteView(DeleteView):
    model = NewCustomer
    template_name='delete.html'
    success_url ="/core/"


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


class customerUpdateView(UpdateView):
    model = NewCustomer
    template_name='update.html'
    success_url ="/core/"

    form_class = CustomerForm

def form_valid(self, form):
        form.instance.user = self.request.user
        return super(customerUpdateView,self).form_valid(form)


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'registration/register.html' , {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html' , {'form': form}) 


