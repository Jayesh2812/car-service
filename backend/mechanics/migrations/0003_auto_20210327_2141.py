# Generated by Django 3.1.7 on 2021-03-27 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mechanics', '0002_bookingrequest_vehicletype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrequest',
            name='assignedMechanic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mechanics.mechanic'),
        ),
    ]
