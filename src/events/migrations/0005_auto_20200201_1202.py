# Generated by Django 2.2.9 on 2020-02-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20200201_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comitees',
            name='notes',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]