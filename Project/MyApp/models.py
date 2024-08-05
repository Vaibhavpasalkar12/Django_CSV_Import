from django.db import models

# Create your models here.
class EmpD(models.Model):
    EId = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Experience = models.IntegerField()
    Position = models.CharField(max_length=500)
    Salary = models.IntegerField()