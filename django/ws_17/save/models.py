from django.db import models

class Save(models.Model):   #모델명은 단수가 일반적
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    birthday = models.DateField()
    age = models.IntegerField()
        
    def __str__(self):
        return self.name 

# Create your models here.
