# Generated by Django 4.2.5 on 2023-09-15 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='bookId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_general.booking'),
        ),
    ]
