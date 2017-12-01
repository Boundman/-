from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=5, label='Login')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Repeat Password')
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')


class EnterForm(forms.Form):
    username = forms.CharField(label='Login')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
