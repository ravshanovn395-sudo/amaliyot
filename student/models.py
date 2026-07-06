from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=150)  
    age = models.IntegerField() 
    number = models.CharField(max_length=20)  

    def __str__(self):
        return self.name