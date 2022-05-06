# Generated by Django 2.2.5 on 2022-05-01 08:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='relationship',
            field=models.ManyToManyField(blank=True, related_name='_customuser_relationship_+', to=settings.AUTH_USER_MODEL),
        ),
    ]