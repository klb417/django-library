# Generated by Django 3.0.3 on 2020-02-07 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year_published',
            field=models.IntegerField(),
        ),
    ]
