# Generated by Django 3.0.6 on 2020-05-09 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0003_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='from_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='availability',
            name='to_date',
            field=models.DateField(),
        ),
    ]