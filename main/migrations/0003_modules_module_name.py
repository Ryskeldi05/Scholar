# Generated by Django 3.2.4 on 2021-06-17 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210615_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='modules',
            name='module_name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]