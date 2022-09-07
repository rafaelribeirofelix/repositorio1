import email
from django import forms
from django.shortcuts import render
from  django import  forms 

from polls.models import Webpage


class MyNewForm(forms.ModelForm):
    class Meta:
        model = Webpage
        fields = "__all__"

class NameForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

