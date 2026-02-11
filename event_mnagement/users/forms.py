from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Membership

class CustomUserCreationForm(UserCreationForm):
    membership = forms.ModelChoiceField(
        queryset=Membership.objects.all(),
        required=False
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'membership', 'password1', 'password2')
