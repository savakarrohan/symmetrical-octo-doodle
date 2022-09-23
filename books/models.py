from django.db import models

# Create your models here.
class Book(models.Model):
    """database of books"""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    def __str__(self):
        return self.title