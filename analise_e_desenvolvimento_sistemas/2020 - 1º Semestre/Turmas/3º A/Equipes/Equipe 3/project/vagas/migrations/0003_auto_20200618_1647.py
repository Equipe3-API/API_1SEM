# Generated by Django 2.2 on 2020-06-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0002_auto_20200618_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='curriculo',
            field=models.FileField(upload_to='documents/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='habilidades',
            field=models.ManyToManyField(blank=True, to='vagas.Habilidades'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='numero_end',
            field=models.CharField(max_length=250, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='rua',
            field=models.CharField(max_length=250, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='candidato',
            field=models.ManyToManyField(blank=True, to='vagas.Candidato', verbose_name='Candidatos Cadastrados'),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='competencia',
            field=models.ManyToManyField(blank=True, to='vagas.Competencia', verbose_name='Competências da Vaga'),
        ),
    ]
