from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"