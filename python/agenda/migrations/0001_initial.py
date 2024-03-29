# Generated by Django 3.2.6 on 2021-08-10 02:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.BigIntegerField(default=True, primary_key=True, serialize=False)),
                ('quarto', models.IntegerField()),
                ('servico_de_quarto', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('rg', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('senha', models.CharField(max_length=50)),
                ('data_de_cadastro', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='uniqueid', primary_key=True, serialize=False)),
                ('dias', models.IntegerField()),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='agenda.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Limpeza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faxina', models.BooleanField(default=False)),
                ('horarios', models.TimeField(default=True)),
                ('quarto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.checkin')),
            ],
        ),
        migrations.CreateModel(
            name='CheckOut',
            fields=[
                ('id', models.BigIntegerField(default=True, primary_key=True, serialize=False)),
                ('despesas', models.IntegerField()),
                ('quarto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='agenda.checkin')),
                ('usuario', models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to='agenda.usuarios')),
            ],
        ),
        migrations.AddField(
            model_name='checkin',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='agenda.usuarios'),
        ),
    ]
