from django.db import models

class Person(models.Model):
    data1 = models.CharField(max_length=100)
    data2 = models.IntegerField()
    data3 = models.CharField(max_length=100)

