# Generated by Django 5.0.2 on 2024-02-21 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0002_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefone',
            field=models.TextField(default=''),
        ),
    ]