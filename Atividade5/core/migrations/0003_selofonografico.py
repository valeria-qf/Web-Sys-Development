# Generated by Django 4.2.6 on 2023-10-11 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_discos_ano_alter_discos_quantidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeloFonografico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('disco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.discos')),
            ],
        ),
    ]
