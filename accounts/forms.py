# Creating this file to change the default form available from the django admin site to our USER model
from django.contrib.auth import get_user_model
# User creation and user change forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
class CustomUserCreationForm(UserCreationForm):
    """Custom User Creation form on admin update for appropriate fields
    password field implicitly included"""
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )
class CustomUserChangeForm(UserChangeForm):
    """Custom User change form on admin, update for appropriate fields
    password field implicitly included"""
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )