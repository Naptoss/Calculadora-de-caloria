from dataclasses import field
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm


class fooditemForm(ModelForm):
    class Meta:
        model = Fooditem
        field = "__all__"


class addUserFooditem(ModelForm):
    class Meta:
        model = UserFoodItem
        fiels = "__all__"


class createUserForm(UserCreationForm):
    class Meta:
        model = User
        field = ['username', 'email', 'password1', 'password2']
