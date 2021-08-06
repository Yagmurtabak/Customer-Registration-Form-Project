from django.shortcuts import redirect, render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView,FormView
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q


from .forms import CustomerForm
from .models import Customer


class CustomerListView(ListView):
    template_name = 'list.html'
    model = Customer
    context_object_name = 'allcustomers'
    paginate_by = 5

    def get_queryset(self):

        word = self.request.GET.get("word")
        if word:
            return Customer.objects.filter(
            Q(name__icontains=word)|
            Q(surname__icontains=word)|
            Q(tc__icontains=word)|
            Q(city__icontains=word)|
            Q(district__icontains=word)|
            Q(telephone__icontains=word)).order_by('-date')
        return Customer.objects.all().order_by('-date')
            



class CustomerDetailView(DetailView):
    template_name = 'detail.html'
    model = Customer
    context_object_name = 'Customer'


class CustomerCreateView(CreateView):
    template_name = 'create.html'
    form_class = CustomerForm
    success_url = ""

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CustomerCreateView,self).form_valid(form)


class CustomerView(FormView):
    template_name = 'sent.html'
    form_class = CustomerForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()    
        else:
            return render(request, "create.html",{"form":form})

        return render(request, self.template_name, {'form': form})

 
class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'delete.html'
    success_url = "/"


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'update.html'
    success_url = "/"

    form_class = CustomerForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CustomerUpdateView,self).form_valid(form)


class RegisterationView(FormView):
    template_name = 'registration/register.html'

    form_class = UserCreationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
        else:
            return render(request, "registration/register.html",{"form":form})

    

