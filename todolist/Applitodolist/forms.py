from django import forms
from .models import Task


""""class ConnexionForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password']
        name = forms.CharField(label='Nom', max_length= 100, required=True)
        password = forms.CharField(label='Password', max_length= 30, required= True)"""


class SimpleForm(forms.Form):
    name = forms.CharField(max_length= 100, label="Nom")
    password = forms.CharField(widget=forms.PasswordInput, label= "Password")


class TaskForm (forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed', 'finish_date', 'priority']
        widgets = {'title': forms.TextInput(attrs= {'placeholder': 'titre', 'label': ' '})}


