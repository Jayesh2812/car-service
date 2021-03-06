# Generated by Django 3.1.7 on 2021-03-27 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNo', models.DecimalField(decimal_places=0, max_digits=10)),
                ('centerName', models.CharField(max_length=300)),
                ('openingTime', models.TimeField()),
                ('closingTime', models.TimeField()),
                ('locationState', models.CharField(max_length=200)),
                ('locationCity', models.CharField(max_length=200)),
                ('locationPinCode', models.DecimalField(decimal_places=0, max_digits=6)),
                ('address', models.CharField(max_length=500)),
                ('numberOfMechs', models.DecimalField(decimal_places=0, max_digits=4)),
                ('baseVisitingCharges', models.DecimalField(decimal_places=2, max_digits=4)),
                ('availableServices', models.CharField(max_length=800)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
