# Generated by Django 4.2.19 on 2025-02-27 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_details_complaint_details_complaint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='ps_io_number',
        ),
        migrations.AddField(
            model_name='complaint',
            name='ps_io_number',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
