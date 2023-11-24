# Generated by Django 4.2.2 on 2023-11-17 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(max_length=200, verbose_name='Nome do cliente')),
                ('email', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartamento', models.IntegerField()),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Hospedagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateField(verbose_name='Data de entrada')),
                ('data_saida', models.DateField(verbose_name='Data de saída')),
                ('valor', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospedagem.cliente')),
                ('quarto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospedagem.quarto')),
            ],
        ),
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('data', models.DateField(verbose_name='Data')),
                ('valor', models.FloatField()),
                ('hospedagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospedagem.hospedagem')),
            ],
        ),
    ]