from django.contrib import admin
# get default user model mentioned in settings file
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.
# Custom forms imported from forms
from .forms import CustomUserChangeForm,CustomUserCreationForm

# Custom User from the default method
CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    """Class based view? for the custom model and it's appropriate views"""
    # User creation form depicted by variable add_form and so on
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_superuser",
    ]
# Registers the CustomUser model to the administrator, thus allowing them to access it?
admin.site.register(CustomUser,CustomUserAdmin)
