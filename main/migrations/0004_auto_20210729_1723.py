# Generated by Django 3.2.4 on 2021-07-29 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_mentors_courses'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Блог'},
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name': 'Контент', 'verbose_name_plural': 'Контенты'},
        ),
        migrations.AlterModelOptions(
            name='content_type',
            options={'verbose_name': 'Тип контента'},
        ),
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AlterModelOptions(
            name='mentors',
            options={'verbose_name': 'Ментор', 'verbose_name_plural': 'Менторы'},
        ),
        migrations.AlterModelOptions(
            name='modules',
            options={'verbose_name': 'Модуль', 'verbose_name_plural': 'Модули'},
        ),
    ]
