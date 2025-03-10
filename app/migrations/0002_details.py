# Generated by Django 3.1.4 on 2025-02-24 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_details', models.CharField(max_length=200, null=True)),
                ('complaint_details', models.CharField(max_length=100)),
                ('ps_io_number', models.CharField(max_length=100)),
                ('account_balances', models.IntegerField()),
                ('transaction_amount', models.IntegerField()),
                ('disputed_amount', models.CharField(max_length=100)),
                ('frezz', models.CharField(max_length=100)),
                ('layer', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('update', models.CharField(max_length=200)),
            ],
        ),
    ]
