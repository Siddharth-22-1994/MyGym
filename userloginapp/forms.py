from django import forms

from django.contrib.auth import (
    authenticate,
    get_user_model
)

class userloginform(forms.Form):

    # https: // www.youtube.com / watch?v = _oMY2o2NhWM ---> You tube link for --> attrs
    uname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            }
    ))
    paswd = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data['uname']
        password = self.cleaned_data['paswd']

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')

        return super(userloginform, self).clean(*args, **kwargs)

