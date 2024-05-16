import re
from django import forms
from . models import Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    
    def clean_name(self):
        name = self.cleaned_data['name']

        if bool(re.search(r'\d', str(name))):
            raise forms.ValidationError("Invalid  Name.")
        return name
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels= {
            'username':'Username', 'first_name':'First Name', 'last_name':'Last Name',
            'email':'Email'
        }
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
