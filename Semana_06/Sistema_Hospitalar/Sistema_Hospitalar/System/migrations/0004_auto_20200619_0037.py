# Generated by Django 3.0.7 on 2020-06-19 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0003_auto_20200619_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='municipios',
            name='Nome',
        ),
        migrations.RemoveField(
            model_name='municipios',
            name='cod_Municipio',
        ),
        migrations.AddField(
            model_name='instituicoes',
            name='tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='System.Tipo_Instituicao'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='municipios',
            name='cod_municipio',
            field=models.CharField(default=1, max_length=5, verbose_name='Código'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='municipios',
            name='nome',
            field=models.CharField(default='1', max_length=60, verbose_name='Município'),
            preserve_default=False,
        ),
    ]
