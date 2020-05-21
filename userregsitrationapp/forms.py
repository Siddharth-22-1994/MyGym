from django import forms

from django.contrib.auth import (
    authenticate,
    get_user_model
)

User = get_user_model()


class userregisterform(forms.ModelForm):
    email = forms.EmailField(label='Email Adress')
    email2 = forms.EmailField(label='Confirm Email')
    passowrd = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'passowrd',

        ]
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')


        if email != email2:
            raise forms.ValidationError('email must match')
        email_qs = User.objects.filter(email=email)
        if email_qs:
            raise forms.ValidationError('This email is already being used')


        return super(userregisterform, self).clean(*args, **kwargs)
