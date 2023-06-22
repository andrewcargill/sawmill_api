from django.db import models
from django.utils import timezone
from dropbox import Dropbox
from django.conf import settings
from dropbox.files import WriteMode, DeleteError


class Test(models.Model):
    longitude = models.DecimalField(max_digits=16, decimal_places=14, blank=True, null=True)
    latitude = models.DecimalField(max_digits=16, decimal_places=14, blank=True, null=True)
    data1 = models.CharField(max_length=100)
    data2 = models.IntegerField()
    data3 = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

from django.db import models
from dropbox import Dropbox
from django.conf import settings

class DropboxTest(models.Model):
    file = models.FileField(upload_to='dropbox_files/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Upload the file to Dropbox
        dropbox = Dropbox(settings.DROPBOX_ACCESS_TOKEN)
        with open(self.file.path, 'rb') as f:
            dropbox.files_upload(f.read(), f"/{self.file.name}", mode=WriteMode('overwrite'))

    def delete(self, *args, **kwargs):
        # Delete the file from Dropbox
        dropbox = Dropbox(settings.DROPBOX_ACCESS_TOKEN)
        dropbox.files_delete_v2(f"/{self.file.name}")

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

class MoistureCheck(models.Model):
    plank = models.ForeignKey(Plank, on_delete=models.CASCADE)
    date = models.DateField()
    water_percentage = models.DecimalField(max_digits=5, decimal_places=2)
