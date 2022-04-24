from django import forms
from .models import ContactProfile


class ContactForm(forms.ModelForm):

    name = forms.CharField(max_length=50, required=True,
                           widget=forms.TextInput(attrs={
                               'placeholder': '*Full name..',
                           }))
    email = forms.EmailField(max_length=254, required=True,
                             widget=forms.TextInput(attrs={
                                 'placeholder': '*Email..',
                             }))

    message = forms.CharField(max_length=200, required=True, widget=forms.Textarea(attrs={'placeholder': '*Message',
                                                                                          'rows': 4,
                                                                                          }))

    class Meta:
        model = ContactProfile

        fields = ('name', 'email', 'message')
