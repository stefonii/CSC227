# Generated by Django 2.2.5 on 2020-05-11 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('bug_id', models.AutoField(primary_key=True, serialize=False)),
                ('bug_name', models.TextField()),
                ('bug_value', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Bug',
                'verbose_name_plural': 'Bugs',
                'db_table': 'Bug',
                'managed': False,
            },
        ),
    ]
