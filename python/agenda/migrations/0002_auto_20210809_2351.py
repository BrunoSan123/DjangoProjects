# Generated by Django 3.2.6 on 2021-08-10 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='id',
            field=models.BigIntegerField(auto_created=True, default=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='id',
            field=models.BigIntegerField(auto_created=True, default=True, primary_key=True, serialize=False),
        ),
    ]
