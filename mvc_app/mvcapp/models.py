from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    fees = models.FloatField()
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    dept = models.CharField(max_length=30)

    class Meta:
        db_table = 'STUDENT_MASTER'

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)