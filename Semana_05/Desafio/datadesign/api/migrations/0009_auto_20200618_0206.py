# Generated by Django 3.0.6 on 2020-06-18 05:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200618_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='address',
            field=models.GenericIPAddressField(validators=[django.core.validators.validate_ipv4_address], verbose_name='Endereço de IP'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator], verbose_name='Senha'),
        ),
    ]
