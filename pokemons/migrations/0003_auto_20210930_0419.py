# Generated by Django 3.2.5 on 2021-09-30 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0002_auto_20210928_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ginasios',
            old_name='nome',
            new_name='nome_do_ginasio',
        ),
        migrations.RenameField(
            model_name='territorios',
            old_name='nome',
            new_name='nome_do_territorio',
        ),
        migrations.RenameField(
            model_name='treinador',
            old_name='nome',
            new_name='nome_do_treinador',
        ),
    ]