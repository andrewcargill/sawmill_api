from django.db import models
from django.utils import timezone
# from dropbox import Dropbox
from django.conf import settings
# from dropbox.files import WriteMode, DeleteError
from storages.backends.dropbox import DropBoxStorage
from dropbox.exceptions import ApiError




class Test(models.Model):
    longitude = models.DecimalField(max_digits=16, decimal_places=14, blank=True, null=True)
    latitude = models.DecimalField(max_digits=16, decimal_places=14, blank=True, null=True)
    data1 = models.CharField(max_length=100)
    data2 = models.IntegerField()
    data3 = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

class DropboxTest(models.Model):
    file = models.FileField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        try:
            # Upload the file to Dropbox using the DropBoxStorage backend
            storage = DropBoxStorage()
            file_path = f"/{self.file.name}"
            storage.save(file_path, self.file)
        except ApiError as e:
            # Handle any Dropbox API errors
            print(f"Error uploading file to Dropbox: {e}")

    def delete(self, *args, **kwargs):
        # Delete the file from Dropbox using the DropBoxStorage backend
        storage = DropBoxStorage()
        file_path = f"/{self.file.name}"
        storage.delete(file_path)

        super().delete(*args, **kwargs)



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
    live_edge = models.BooleanField(default=False)
    furniture = models.BooleanField(default=False)
    structural = models.BooleanField(default=False)
    general = models.BooleanField(default=False)
    info = models.TextField(default='No extra information on this wood.')

class MoistureCheck(models.Model):
    plank = models.ForeignKey(Plank, on_delete=models.CASCADE)
    date = models.DateField()
    water_percentage = models.DecimalField(max_digits=5, decimal_places=2)
