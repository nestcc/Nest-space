# Generated by Django 2.2.5 on 2020-05-06 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200506_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nepuser',
            name='icon',
            field=models.ImageField(null=True, upload_to='user_icon/'),
        ),
    ]