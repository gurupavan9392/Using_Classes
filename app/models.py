from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    slocation=models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('SchoolDetail',kwargs={'pk':self.pk})

    def __str__(self) -> str:
        return self.sname

class Student(models.Model):
    stname=models.CharField(max_length=100)
    stage=models.IntegerField()
    sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    def __str__(self) -> str:
        return self.stname