# Generated by Django 5.1.4 on 2024-12-09 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicationSKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(max_length=255, unique=True)),
                ('formulation', models.CharField(max_length=255)),
                ('dosage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('inn', 'formulation', 'dosage', 'unit')},
            },
        ),
    ]