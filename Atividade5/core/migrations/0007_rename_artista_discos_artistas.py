# Generated by Django 4.2.6 on 2023-10-11 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_artista_discos_artista'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discos',
            old_name='artista',
            new_name='artistas',
        ),
    ]
