# Generated by Django 4.0.3 on 2022-05-30 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_token_refresh_token_alter_token_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='refresh_token',
            field=models.CharField(max_length=2100),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(max_length=2100),
        ),
    ]