# Generated by Django 5.0.1 on 2024-01-27 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0002_remove_employee_firstname_remove_employee_lastname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='password',
        ),
    ]
