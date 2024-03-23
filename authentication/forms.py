# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    location = forms.CharField(max_length=100, required=True)
    name = forms.CharField(max_length=100, required=True)
    surname = forms.CharField(max_length=100, required=True)
    dob = forms.DateField(required=True)
    role = forms.ChoiceField(choices=(('Fixer', 'Fixer'), ('Client', 'Client')), required=True)
    fixer_job = forms.CharField(max_length=20, required=False)  # Optional field for Fixer job
    
    def clean_worker_type(self):
        role = self.cleaned_data.get('role')
        worker_type = self.cleaned_data.get('worker_type')

        if role == CustomUser.WORKER and not worker_type:
            raise forms.ValidationError("Worker type must be specified for workers")
        
        return worker_type

    class Meta:
        model = CustomUser  # Use CustomUser model
        fields = ['username', 'email', 'password1', 'password2', 'location', 'name', 'surname', 'dob', 'role', 'fixer_job']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search')



