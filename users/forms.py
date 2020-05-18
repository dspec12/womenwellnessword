from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("fullname", "username", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("fullname", "username", "email")


class SignupForm(forms.Form):
    fullname = forms.CharField(max_length=30, label="Full Name")

    def signup(self, request, user):
        user.fullname = self.cleaned_data["fullname"]
        user.save()
