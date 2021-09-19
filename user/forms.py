from django import forms
from django.forms.widgets import PasswordInput

class LoginForm(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "Password",widget = PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label = "Username")
    password = forms.CharField(max_length=20, label = "Password", widget= forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label = "Confirm Password", widget=forms.PasswordInput)
    
    
    """ 
    This method is the override method. Through to this method, we want to send the 
    username and password information as a dict structure if the passwords are the same.
    """
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords are not matching.")
        values = {
            "username": username,
            "password": password,
        }
        return values
