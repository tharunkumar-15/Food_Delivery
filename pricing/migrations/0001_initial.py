# Generated by Django 4.2.10 on 2024-02-13 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('perishable', 'Perishable'), ('non-perishable', 'Non-Perishable')], max_length=20)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(max_length=100)),
                ('base_distance_in_km', models.PositiveIntegerField()),
                ('km_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fix_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricing.item')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricing.organization')),
            ],
        ),
    ]
