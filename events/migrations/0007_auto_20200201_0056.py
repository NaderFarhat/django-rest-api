# Generated by Django 2.2.9 on 2020-02-01 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20200201_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='year',
            field=models.CharField(max_length=255),
        ),
    ]
