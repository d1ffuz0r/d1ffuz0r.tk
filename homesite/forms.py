from django import forms
from models import QuickMessages

class QuickContactForm(forms.ModelForm):
    class Meta:
        model = QuickMessages
        fields = ("name", "email", "message")
        widgets = {
            "name": forms.TextInput({"value": u"Name"}),
            "email": forms.TextInput({"value": u"Email"}),
            "message": forms.Textarea(attrs={"cols": 10}),
        }