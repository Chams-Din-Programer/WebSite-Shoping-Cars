# Generated by Django 4.1.7 on 2023-04-29 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_usercontact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserContact',
        ),
    ]