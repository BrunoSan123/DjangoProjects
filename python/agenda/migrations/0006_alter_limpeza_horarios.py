# Generated by Django 3.2.5 on 2021-08-13 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_alter_checkout_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='limpeza',
            name='horarios',
            field=models.TimeField(auto_now=True),
        ),
    ]
