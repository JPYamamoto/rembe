# Generated by Django 4.0.3 on 2022-04-14 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_usuario_tarjeta_autor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarjeta',
            old_name='nombre_tarjeta',
            new_name='nombre',
        ),
    ]