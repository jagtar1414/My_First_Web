# Generated by Django 4.1.4 on 2022-12-14 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_rename_register_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='stresults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rnum', models.CharField(max_length=30)),
                ('nme', models.CharField(max_length=30)),
                ('dob', models.CharField(max_length=30)),
                ('results', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'stdresults',
            },
        ),
    ]
