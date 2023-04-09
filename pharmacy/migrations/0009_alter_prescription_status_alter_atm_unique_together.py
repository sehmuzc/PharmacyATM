# Generated by Django 4.2.dev20221028064633 on 2023-04-08 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0008_prescriptionfulfillment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('dispensed', 'dispensed'), ('cancelled', 'cancelled')], default='active', max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='atm',
            unique_together={('city', 'county')},
        ),
    ]