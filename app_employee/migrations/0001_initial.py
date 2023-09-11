# Generated by Django 4.2.5 on 2023-09-06 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmpID', models.IntegerField(max_length=5, primary_key=True, serialize=False)),
                ('EmpFirstName', models.CharField(max_length=25)),
                ('EmpLastName', models.CharField(max_length=25)),
                ('Job', models.CharField(max_length=15)),
                ('Contract', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='GuideTour',
            fields=[
                ('GuideTour', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Contact', models.CharField(max_length=10)),
                ('Status', models.TextField()),
                ('EmpID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_employee.employees')),
            ],
        ),
    ]