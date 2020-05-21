from django import forms

from BuyProdApp.models import BuyProductModel


class BuyProductForm(forms.ModelForm):
    class Meta:
        model = BuyProductModel
        fields= '__all__'