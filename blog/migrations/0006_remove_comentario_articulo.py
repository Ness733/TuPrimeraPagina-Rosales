# Generated by Django 4.2.3 on 2023-08-15 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comentario_articulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='articulo',
        ),
    ]
