# Generated by Django 4.2.1 on 2023-05-15 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriarelatorio',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=8, null=True),
        ),
    ]
