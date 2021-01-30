from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    """Required and Optional Fields

    Fields which only exist outside Meta are optional. And the fields which
    exist in Meta AND outside Meta (UserRegistrationForm) are required by
    default
    """
    email = forms.EmailField(required=False, label='Email')
    username = forms.CharField(max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput(),
                                label='Enter Password')
    password2 = forms.CharField(widget=forms.PasswordInput(),
                                label='Confirm Password')

    class Meta:
        """Nested name-space for configurations."""
        model = User
        fields = ['email', 'username', 'password1', 'password2']    # order
