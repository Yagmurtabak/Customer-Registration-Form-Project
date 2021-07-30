from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView,FormView

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


class PostUpdateViev(UpdateView):
    model = NewCustomer
    template_name='update.html'
    success_url ="/post/"

    form_class = CustomerForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostUpdateViev,self).form_valid(form)

