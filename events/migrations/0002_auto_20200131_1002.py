# Generated by Django 2.2.9 on 2020-01-31 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='weight',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='year',
            field=models.IntegerField(),
        ),
    ]