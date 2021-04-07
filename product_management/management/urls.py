from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from management.views import signuppage, AddCategory, AddProduct, DeleteProduct, UpdateProduct, ViewCategories, UpdateCategory, DeleteCategory

urlpatterns = [
    path('signup/', signuppage, name='signup'),
    path('add-category/', login_required(AddCategory.as_view()), name='add-category'),
    path('add-product/', login_required(AddProduct.as_view()), name='add-product'),
    path('delete-product/<pk>/',login_required(DeleteProduct.as_view()), name='delete-product'),
    path('update-product/<pk>/',login_required(UpdateProduct.as_view()), name='update-product'),
    path('view-categories/',login_required(ViewCategories.as_view()), name='view-categories'),
    path('update-category/<pk>/',login_required(UpdateCategory.as_view()), name='update-Category'),
    path('delete-category/<pk>/',login_required(DeleteCategory.as_view()), name='delete-category'),
]