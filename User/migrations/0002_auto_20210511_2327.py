# Generated by Django 3.2.2 on 2021-05-11 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastName',
        ),
        migrations.AddField(
            model_name='profile',
            name='fullName',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
