# Generated by Django 2.2.9 on 2020-02-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comitees',
            name='notes',
            field=models.CharField(max_length=255, null=True),
        ),
    ]