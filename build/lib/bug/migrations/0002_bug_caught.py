# Generated by Django 2.2.5 on 2020-05-12 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bug',
            options={'managed': True, 'verbose_name': 'Bug', 'verbose_name_plural': 'Bugs'},
        ),
    ]
