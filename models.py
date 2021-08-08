from django.db import models
class Newuser_details(models.Model):
    name=models.CharField(max_length=200)
    pswd=models.CharField(max_length=100)
    def __str__(self):
        return self.name


# Create your models here.
