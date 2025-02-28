# Generated by Django 4.2.19 on 2025-02-27 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_details_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='complaint_details',
        ),
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_details', models.CharField(max_length=100)),
                ('detail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.details')),
            ],
        ),
    ]
