from django import forms
from .models import Task

class TaskForm (forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed', 'finish_date', 'priority']
        widgets = {'title': forms.TextInput(attrs= {'placeholder': 'titre', 'label': ' '})}


