# Generated by Django 3.0.8 on 2020-07-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200513_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='nepuser',
            name='nick_name',
            field=models.CharField(default='None', max_length=20),
        ),
    ]
