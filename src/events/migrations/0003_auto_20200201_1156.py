# Generated by Django 2.2.9 on 2020-02-01 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200201_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comitees',
            name='notes',
            field=models.TextField(max_length=255, null=True),
        ),
    ]