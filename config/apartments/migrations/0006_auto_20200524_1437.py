# Generated by Django 3.0.6 on 2020-05-24 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0005_auto_20200523_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='apa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availability', to='apartments.Apartment'),
        ),
    ]
