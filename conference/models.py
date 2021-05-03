from django.db import models

# Create your models here.

class Participant(models.Model):
    fullname = models.CharField(max_length=200)
    emails = models.CharField(max_length=200)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=40)
    capacity = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.fullname
        