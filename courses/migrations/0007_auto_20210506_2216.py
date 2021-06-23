# Generated by Django 3.2.1 on 2021-05-06 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0006_auto_20210505_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='courses',
            name='registerd_users',
            field=models.ManyToManyField(blank=True, related_name='mycourses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Teachers',
        ),
    ]