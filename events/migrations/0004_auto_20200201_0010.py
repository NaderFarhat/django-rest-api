# Generated by Django 2.2.9 on 2020-02-01 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20200131_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='height',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='events',
            name='weight',
            field=models.CharField(max_length=255),
        ),
    ]
