# Generated by Django 3.2.4 on 2021-06-25 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20210625_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
