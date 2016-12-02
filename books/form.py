from django.forms import forms

class LenderForm(forms.Form):
    bookNo = forms.CharField()
    title = forms.CharField()
    email = forms.EmailField(required=False)
