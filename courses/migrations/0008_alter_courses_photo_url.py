# Generated by Django 3.2.2 on 2021-05-09 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20210506_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='photo_url',
            field=models.CharField(max_length=500),
        ),
    ]
