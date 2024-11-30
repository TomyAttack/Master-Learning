from django.db import models

# Create your models here.

class Positon(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Employee(models.Model):
    """docstring for Employee"""
    full_name = models.CharField(max_length=255)
    emp_code = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Positon, on_delete=models.CASCADE)
