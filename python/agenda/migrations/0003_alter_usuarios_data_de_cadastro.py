# Generated by Django 3.2.6 on 2021-08-10 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_auto_20210809_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='data_de_cadastro',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]