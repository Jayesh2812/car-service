# Generated by Django 3.1.7 on 2021-03-28 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechanics', '0004_auto_20210327_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrequest',
            name='requestState',
            field=models.IntegerField(choices=[(0, 'pending'), (1, 'accepted'), (2, 'rejected'), (3, 'completed')]),
        ),
    ]