# Generated by Django 2.2.9 on 2020-02-01 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20200201_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='height',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='medal',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='weight',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
