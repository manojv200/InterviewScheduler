# Generated by Django 4.2.11 on 2025-01-24 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblusers',
            name='end_date',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tblusers',
            name='start_date',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
