import email
from pyexpat import model
from django.db import models

# Create your models here.
class Contact (models.Model):
    name = models.CharField( max_length=50)
    email = models.CharField(max_length=50)
    subject= models.TextField(max_length=200)
    message= models.TextField()
    date = models.DateField()