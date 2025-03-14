from django import forms

from .models import Contact

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
            'id': 'email',
            'placeholder': 'Başlıq'
            }),
            'message' : forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'message',
            'placeholder': 'text...'
            })
            
        }


    def clean_email(self):
        value = self.cleaned_data['email']
        if not value.endswith('.com'):
            raise forms.ValidationError('Email must end with .com!')
        
        return value
    
    def clean_name(self):
        value = self.cleaned_data['name']
        if value == 'admin':
            raise forms.ValidationError('Name can not be admin!')
        
        return value