# Generated by Django 4.2.1 on 2023-05-16 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorios', '0002_categoriarelatorio_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatorio',
            name='protocolo',
            field=models.CharField(blank=True, max_length=52, null=True),
        ),
    ]
