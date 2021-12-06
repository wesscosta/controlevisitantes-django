# Generated by Django 3.0 on 2021-12-04 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('porteiros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=194, verbose_name='Nome completo')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('numero_casa', models.PositiveSmallIntegerField(verbose_name='Número da casa a ser visitada')),
                ('placa_veiculo', models.CharField(blank=True, max_length=7, null=True, verbose_name='Placa do veiculo')),
                ('horario_chegada', models.DateTimeField(auto_now_add=True, verbose_name='Horario de chegada na portaria')),
                ('horario_saida', models.DateTimeField(blank=True, null=True, verbose_name='Horario de saida do condominio')),
                ('horario_autorizado', models.DateTimeField(blank=True, null=True, verbose_name='Horario de autorizção de entrada')),
                ('morador_responsavel', models.CharField(blank=True, max_length=194, verbose_name='Nome do morador responsavel por autorizar a entrada do visitante')),
                ('registrador_por', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='porteiros.Porteiro', verbose_name='Porteiro responsavel pelo registro')),
            ],
            options={
                'verbose_name': 'Visitante',
                'verbose_name_plural': 'Visitantes',
                'db_table': 'visitante',
            },
        ),
    ]