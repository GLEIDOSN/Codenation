# Generated by Django 3.0.7 on 2020-06-18 05:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200618_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='env',
            field=models.CharField(blank=True, max_length=20, verbose_name='Env'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='Senha'),
        ),
    ]