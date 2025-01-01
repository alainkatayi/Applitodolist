from django import forms
from django.contrib.auth.forms import AuthenticationForm

class SimpleForm(forms.Form):
    name = forms.CharField(max_length= 100, label="Nom ddd")
  
    password = forms.CharField(widget=forms.PasswordInput, label= "Password")



