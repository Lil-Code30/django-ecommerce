# Generated by Django 5.1.2 on 2024-11-07 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0006_client_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='last_name',
        ),
    ]
