# Generated by Django 4.2.dev20221028064633 on 2023-03-25 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0006_atm_atmmedicine_atm_medicines'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('dispensed', 'Dispensed'), ('cancelled', 'Cancelled')], default='new', max_length=20),
        ),
    ]
