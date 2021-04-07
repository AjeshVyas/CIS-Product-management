from django import forms
from django.contrib.auth.models import User

from management.models import Category, Product

class SignUpForm(forms.ModelForm):

    class Meta:

        model=User
        fields=('username','password','email','first_name','last_name')
        widgets={'password':forms.PasswordInput()}

class AddCategoryForm(forms.ModelForm):

	class Meta:

		model = Category
		fields = ('name',)

class AddProductForm(forms.ModelForm):

    class Meta:

        model = Product
        fields = ('name','thumbnail','tags','description','category')
        widgets = {'description': forms.Textarea()}