from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=120)
    registrationNo = models.CharField(max_length=120)
    cgpa = models.FloatField()

    def __str__(self):
        return self.name
