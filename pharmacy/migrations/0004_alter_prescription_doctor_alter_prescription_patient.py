# Generated by Django 4.2.dev20221028064633 on 2023-03-18 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userprofile_options'),
        ('pharmacy', '0003_alter_medicine_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to='users.userprofile'),
        ),
    ]