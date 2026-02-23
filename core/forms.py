from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Extended signup form that collects additional user profile fields."""

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'phone',
            'bio',
            'password1',
            'password2',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make email required
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        # Add placeholders
        self.fields['username'].widget.attrs['placeholder'] = 'Choose a username'
        self.fields['email'].widget.attrs['placeholder'] = 'your@email.com'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone number (optional)'
        self.fields['bio'].widget.attrs['placeholder'] = 'Tell us about yourself (optional)'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create a password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'
