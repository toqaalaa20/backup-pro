# Generated by Django 4.2.8 on 2023-12-13 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
