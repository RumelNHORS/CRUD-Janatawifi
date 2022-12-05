from django import forms
from . models import User
from django.core import validators


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id', 'date', 'trade_code', 'high', 'low', 'open', 'close', 'volume']

        widgets = {
            'date': forms.TextInput(attrs={'class':'form-control'}),
            'trade_code': forms.TextInput(attrs={'class':'form-control'}),
            'high': forms.TextInput(attrs={'class':'form-control'}),
            'low': forms.TextInput(attrs={'class':'form-control'}),
            'open': forms.TextInput(attrs={'class':'form-control'}),
            'close': forms.TextInput(attrs={'class':'form-control'}),
            'volume': forms.TextInput(attrs={'class':'form-control'}),
        }