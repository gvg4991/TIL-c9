from django.db import models

class Save(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    birthday = models.DateField()
    age = models.IntegerField()
        
    def __str__(self):
        return self.title 

# Create your models here.
