from django.db import models

# Create your models here.
class StudyProgram(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Student(models.Model):
    """docstring for Student"""
    full_name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    studyprogram = models.ForeignKey(StudyProgram, on_delete=models.CASCADE)