# Generated by Django 4.2.2 on 2023-06-29 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lumber', '0021_plank_image_tree_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plank',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='plank',
            name='image2',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
