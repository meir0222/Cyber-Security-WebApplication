# Generated by Django 4.1.3 on 2023-01-05 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.IntegerField()),
                ('cust_name', models.CharField(max_length=1000)),
                ('cust_email', models.EmailField(max_length=254)),
                ('cust_contact', models.CharField(max_length=1000)),
            ],
        ),
    ]
