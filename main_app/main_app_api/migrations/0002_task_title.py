# Generated by Django 3.0.5 on 2020-04-22 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='unknown', max_length=200),
            preserve_default=False,
        ),
    ]
