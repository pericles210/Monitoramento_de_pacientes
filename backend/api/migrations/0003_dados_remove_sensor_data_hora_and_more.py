# Generated by Django 4.0.2 on 2022-02-11 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_paciente_telefone_responsavel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dados',
            fields=[
                ('Id_Sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.sensor')),
                ('Temperatura', models.FloatField(blank=True, max_length=10)),
                ('Pressao', models.FloatField(blank=True, max_length=10)),
                ('Oxigenacao', models.FloatField(blank=True, max_length=10)),
                ('Frequencia_Cardiaca', models.FloatField(blank=True, max_length=10)),
                ('Data_Hora', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='Data_Hora',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='Frequencia_Cardiaca',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='Oxigenacao',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='Pressao',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='Temperatura',
        ),
    ]
