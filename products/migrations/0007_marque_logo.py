# Generated by Django 4.1.7 on 2023-04-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_marque_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='marque',
            name='logo',
            field=models.FileField(default=0, upload_to='photos/%y/%m/%d'),
        ),
    ]
