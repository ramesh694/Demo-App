from django import forms
from .models import*
# creating a form corresponding to a model

class EmpForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['first_name','last_name','dob','email']


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']        