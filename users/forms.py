from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# This is the new file that is created to put in the new forms that can inherit from the UserCreationForm

# here I inherit from the UserCreationForm. And I added the addition fields which i want to the UserCreationForm, which in this
# case is the email field by using this "email = forms.EmailField()" code.
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User

        # These are the fields that will be displayed on the forms
        fields = ['username', 'email', 'password1', 'password2']