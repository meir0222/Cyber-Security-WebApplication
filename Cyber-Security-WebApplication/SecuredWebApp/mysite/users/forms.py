from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from users.models import Customer



class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password = forms.CharField()

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class ValidationForm(forms.Form):
    validation_number = forms.CharField(max_length=1000)

