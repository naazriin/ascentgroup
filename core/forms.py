from django import forms
from .models import Contact

import re


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name' : forms.TextInput(attrs={
                'class': 'input-contact',
                'id': 'name',
                'placeholder': 'Adınız'
            }),
            'email' : forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Emailiniz'
            }),
            'subject' : forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'subject',
            'placeholder': 'Başlıq'
            }),
            'message' : forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'message',
            'placeholder': 'text...'
            })
            
        }




    def clean_email(self):
            email = self.cleaned_data.get('email')
            email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

            if not re.match(email_regex, email.strip()):
                raise forms.ValidationError("Invalid email format.")

            return email



    def clean_name(self):
        value = self.cleaned_data.get('name').strip().lower()
        forbidden_names = {'admin', 'root', 'superuser'}

        if value in forbidden_names:
            raise forms.ValidationError('This name is not allowed. Please choose a valid name.')
        
        return value