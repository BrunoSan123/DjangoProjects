# Generated by Django 3.2.5 on 2021-08-13 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0007_alter_limpeza_horarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='limpeza',
            name='id',
        ),
        migrations.AlterField(
            model_name='limpeza',
            name='quarto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='agenda.checkin'),
        ),
    ]
