# Generated by Django 4.2.4 on 2023-08-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='release_year',
            field=models.IntegerField(),
        ),
    ]
