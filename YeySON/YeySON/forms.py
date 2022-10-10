from django import forms

class CommitteeForm(forms.Form):
    title = forms.CharField(label='Suggestion', max_length=128)

class ContactForm(forms.Form):
    committee = forms.CharField(label='Suggestion', max_length=128)
    name = forms.CharField(label='Suggestion', max_length=128)
    position = forms.CharField(label='Suggestion', max_length=128)
    mail = forms.CharField(label='Suggestion', max_length=128)
