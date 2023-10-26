# myapp/forms.py

from django import forms
from .models import Answer

class CompanyValueForm(forms.Form):
    Company_Name= forms.CharField(widget=forms.TextInput)
    Describe_your_industry = forms.CharField(
    widget=forms.Textarea(attrs={'rows': 4, 'cols': 60})
    )
    What_is_your_niche_or_What_services_do_you_offer= forms.CharField(
    widget=forms.Textarea(attrs={'rows': 4, 'cols': 60})
    )
    Describe_your_main_clients_or_client_type= forms.CharField(
    widget=forms.Textarea(attrs={'rows': 4, 'cols': 60})
    )


class PersonValueForm(forms.Form):
    Answer_1 = forms.CharField(
    widget=forms.Textarea(attrs={'rows': 4, 'cols': 60})
    )
    Answer_2 = forms.CharField(
    widget=forms.Textarea(attrs={'rows': 4, 'cols': 60})
    )
    Answer_3 = forms.CharField(
    widget=forms.Textarea(attrs={'rows': 4, 'cols': 60})
    )
    Answer_4 = forms.CharField(
    widget=forms.Textarea(attrs={'rows': 4, 'cols': 60})
    )


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_1', 'answer_2', 'answer_3', 'answer_4']

