# Generated by Django 4.1.6 on 2023-02-10 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_user_is_superuser'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
