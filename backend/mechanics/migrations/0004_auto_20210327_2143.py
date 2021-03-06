# Generated by Django 3.1.7 on 2021-03-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechanics', '0003_auto_20210327_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrequest',
            name='bill',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='bookingrequest',
            name='mechanicArrivalTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookingrequest',
            name='problemDescriptionByMech',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='bookingrequest',
            name='requestAcceptanceTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookingrequest',
            name='serviceCompleteTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
