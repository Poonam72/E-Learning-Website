# Generated by Django 2.2.4 on 2019-12-07 06:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20191011_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Enrollment_ID',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]