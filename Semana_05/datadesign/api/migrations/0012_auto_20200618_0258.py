# Generated by Django 3.0.6 on 2020-06-18 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200618_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='level',
            field=models.CharField(choices=[('CRITICAL', 'Critical'), ('DEBUG', 'Debug'), ('ERROR', 'Error'), ('WARNING', 'Warning'), ('INFOR', 'Infor')], max_length=20, verbose_name='level'),
        ),
    ]