# Generated by Django 3.2.7 on 2021-09-03 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210903_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.SmallIntegerField(null=True, verbose_name='Возраст'),
        ),
    ]
