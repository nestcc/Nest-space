# Generated by Django 2.2.5 on 2020-05-13 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200507_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nepuser',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='nepuser',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]