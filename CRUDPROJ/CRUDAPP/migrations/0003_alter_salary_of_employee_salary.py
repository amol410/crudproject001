# Generated by Django 5.1.3 on 2024-12-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDAPP', '0002_salary_of_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary_of_employee',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
