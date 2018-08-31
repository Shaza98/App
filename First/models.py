from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True )
    phone = models.CharField(max_length=11)
    age = models.IntegerField(max_length=11, blank=True)
    gender = models.CharField(max_length=30, blank=True)
    comment = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

