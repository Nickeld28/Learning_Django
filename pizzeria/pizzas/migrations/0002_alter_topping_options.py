# Generated by Django 4.0.2 on 2022-02-26 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name_plural': 'something'},
        ),
    ]