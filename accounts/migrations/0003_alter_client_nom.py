# Generated by Django 4.1.7 on 2023-04-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_client_prenom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='nom',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
