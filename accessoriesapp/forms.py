from django import forms

from accessoriesapp.models import prodmodel


class prodform(forms.ModelForm):
    class Meta:
        model = prodmodel
        fields = '__all__'