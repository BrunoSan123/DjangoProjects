# Generated by Django 3.2.5 on 2021-10-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0003_auto_20210930_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='treinador',
            name='senha',
            field=models.CharField(max_length=255, null=True),
        ),
    ]