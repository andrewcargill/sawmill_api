# Generated by Django 4.2.2 on 2023-06-27 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lumber', '0014_alter_dropboxtest_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='plank',
            name='live_edge',
            field=models.BooleanField(default=False),
        ),
    ]
