from django.db import models
# Import for user models
# Importing AbstractUser that can later be extended to AbstractBaseUser
from django.contrib.auth.models import AbstractUser
# Create your models here.
# Custom User model
class CustomUser(AbstractUser):
    """Custom User model for simple implementation
        can grow into AbstractBaseUser"""
    pass 