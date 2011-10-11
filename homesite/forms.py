from django import forms
from models import QuickMessages
_ = lambda x: x

class QuickContactForm(forms.ModelForm):
    class Meta:
        model = QuickMessages
        fields = ('name', 'email', 'message')
        widgets = {
            'name' : forms.TextInput({'value':_('Name')}),
            'email' : forms.TextInput({'value':_('Email')}),
            'message' : forms.Textarea(attrs={'cols':10}),
        }