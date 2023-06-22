from django.db import models
from django.utils import timezone


class Test(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    data1 = models.CharField(max_length=100)
    data2 = models.IntegerField()
    data3 = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)


class Tree(models.Model):
    date = models.DateField()
    species = models.CharField(max_length=100)
    reason_for_felling = models.TextField()

class Log(models.Model):
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    date = models.DateField()
    length = models.DecimalField(max_digits=5, decimal_places=2)

class Plank(models.Model):
    date = models.DateField(blank=True, default=timezone.now)
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    depth = models.DecimalField(max_digits=5, decimal_places=2)
    wood_grade = models.CharField(max_length=50)

class MoistureCheck(models.Model):
    plank = models.ForeignKey(Plank, on_delete=models.CASCADE)
    date = models.DateField()
    water_percentage = models.DecimalField(max_digits=5, decimal_places=2)
