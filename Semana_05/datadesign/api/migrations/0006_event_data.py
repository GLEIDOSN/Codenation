# Generated by Django 3.0.6 on 2020-06-18 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200618_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='data',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
