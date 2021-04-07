from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse

from management.forms import SignUpForm, AddCategoryForm, AddProductForm
from management.models import Product, Category

# Create your views here.

def signuppage(request):
    signupform=SignUpForm()
    dict_data = {'signupform':signupform}
    if request.method=='POST':
        signupform=SignUpForm(request.POST)
        user=signupform.save()
        user.set_password(user.password)
        user.save()
        dict_data.update({'msg':'Registered Successfully'})
    return render(request,'management/signup.html',dict_data)

def home(request):
    if request.user.is_authenticated:
        products = Product.objects.filter(user = request.user)
        data = {
            'products':products,
        }
        print(data)
        return render(request,'management/landing.html',data)
    else:
        return render(request,'management/landing.html')

class AddCategory(CreateView):
    model=Category
    fields = ('name',)
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(AddCategory,self).form_valid(form)
    def get_success_url(self):
        return reverse('landing')

class AddProduct(CreateView):
    model=Product
    fields = ('name','thumbnail','tags','description','category')
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(AddProduct,self).form_valid(form)
    def get_success_url(self):
        return reverse('landing')

class DeleteProduct(DeleteView):
    model = Product
    def get_success_url(self):
        return reverse('landing')

class UpdateProduct(UpdateView):
    model=Product
    fields=('name','thumbnail','tags','description','category')
    def get_success_url(self):
            return reverse('landing')

class ViewCategories(ListView):
    model = Category
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

class UpdateCategory(UpdateView):
    model = Category
    fields = ('name',)
    def get_success_url(self):
        return reverse('view-categories')

class DeleteCategory(DeleteView):
    model = Category
    def get_success_url(self):
        return reverse('view-categories')