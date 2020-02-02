# Generated by Django 2.2.9 on 2020-02-02 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comitees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noc', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('notes', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.SmallIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=255, null=True)),
                ('height', models.CharField(max_length=255, null=True)),
                ('weight', models.CharField(max_length=255, null=True)),
                ('team', models.CharField(max_length=255)),
                ('games', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('season', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('sport', models.CharField(max_length=255)),
                ('event', models.CharField(max_length=255)),
                ('medal', models.CharField(max_length=255, null=True)),
                ('noc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Comitees')),
            ],
        ),
    ]
