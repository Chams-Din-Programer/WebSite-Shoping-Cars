# Generated by Django 4.1.7 on 2023-04-13 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_marque_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='id_marque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.marque'),
        ),
    ]
