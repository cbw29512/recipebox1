# Generated by Django 3.0.5 on 2020-05-04 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebox', '0002_auto_20200429_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
