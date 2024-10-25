from django.db import models

# Create your models here.
# # declare a new model with a name "GeeksModel"
# class GeeksModel(models.Model):

#     # fields of the model
#     title = models.CharField(max_length = 200)
#     description = models.TextField()

#     # renames the instances of the model
#     # with their title name
#     def __str__(self):
#         return self.title

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
