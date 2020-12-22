from django.db import models

# Create your models here.

course_options = (
     ('btech','btech'),
     ('mtech','mtech'),
     ('bcom','bcom')

)

class student(models.Model):
    first_name = models.CharField(max_lenght=40)
    last_name = models.CharField(max_lenght=40)
    dob = models.DateField()


def __str__(self):
    return self.first_name +" "+ self.last_name




