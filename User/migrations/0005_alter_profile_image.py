# Generated by Django 3.2.4 on 2021-06-25 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_remove_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='img/sarah.png', upload_to='img/'),
        ),
    ]
