from django.db import models

# Create your models here.

class Place(models.Model):
    
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name  #To view name of places instead of objects
    

class Hotel(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='hotels')
    desc=models.TextField()
    ratings=models.TextField()

    def __str__(self):
        return self.name
    

    