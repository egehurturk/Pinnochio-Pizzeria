from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    """
    User Registration Form - Default Django Form (Inherited from UserCreationForm)

    FIELDS: Username, Password (hashed), Email, First Name, Last Name/

    """

    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
