# Generated by Django 4.2.2 on 2023-06-26 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lumber', '0013_alter_dropboxtest_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropboxtest',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
