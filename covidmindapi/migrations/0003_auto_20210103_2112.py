# Generated by Django 3.1.4 on 2021-01-03 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidmindapi', '0002_auto_20210103_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='link',
            field=models.URLField(),
        ),
    ]