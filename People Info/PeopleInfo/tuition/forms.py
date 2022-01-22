from tkinter.ttk import Widget
from xml.dom.minidom import Attr
from django.forms import ModelForm
from .models import Contact, Post
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        # another contactform class
class ContactFormtwo(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude= ['user','id','created_at','slug']
        Widgets={
            'subject':forms.CheckboxSelectMultiple(attrs={
                'multiple':True,
            }),
            'class_in':forms.CheckboxSelectMultiple(attrs={
                'multiple':True,
            }),
        }
        