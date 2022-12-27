from django.forms import ModelForm
from .models import ClientComment
from django import forms
from django.contrib.auth.models import User

        
class EmailForm(forms.Form):
    your_email = forms.EmailField();
    subject = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea)



