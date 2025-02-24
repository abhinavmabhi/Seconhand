from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        widgets = {
            'category':forms.Select(attrs={'class': 'form-control'}),
            'brand':forms.Select(attrs={'class': 'form-control'}),
            'model':forms.Select(attrs={'class': 'form-control'}),
            'year_of_manufacture':forms.NumberInput(attrs={'class': 'form-control'}),
            'price':forms.NumberInput(attrs={'class': 'form-control'}),
            'kilometers_driven':forms.NumberInput(attrs={'class': 'form-control'}),
            'ownership_status':forms.Select(attrs={'class': 'form-control'}),
        }
