# Generated by Django 4.1.6 on 2023-03-07 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_alter_comment_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='status',
            field=models.CharField(choices=[('ACTIV', 'Активный'), ('NOT_ACTIVE', 'Не активный')], default='ACTIV', max_length=20, verbose_name='Статус'),
        ),
    ]
