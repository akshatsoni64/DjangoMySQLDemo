from django import forms
from .models import SampleModel


class SampleForm(forms.ModelForm):
    no = forms.IntegerField()
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Name Here..'
        }
    ))

    class Meta:
        model = SampleModel
        fields = ('no', 'name', )
