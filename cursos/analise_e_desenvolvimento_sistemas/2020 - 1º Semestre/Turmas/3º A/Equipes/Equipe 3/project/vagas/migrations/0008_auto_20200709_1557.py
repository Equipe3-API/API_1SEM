# Generated by Django 2.2 on 2020-07-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0007_vaga_beneficios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='status',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Ativo'), (2, 'Inativo')], null=True),
        ),
    ]
