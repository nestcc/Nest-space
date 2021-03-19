# Generated by Django 3.1.7 on 2021-03-19 13:48

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NepArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='None Title', max_length=50)),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('update_time', models.DateTimeField(null=True)),
                ('view_time', models.IntegerField(default=0)),
                ('content', ckeditor.fields.RichTextField(null=True)),
                ('key_words', models.CharField(blank=True, max_length=100, null=True)),
                ('is_original', models.BooleanField(default=True)),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('cover_image', models.ImageField(blank=True, default='article_image/default_cover.jpg', null=True, upload_to='article_image')),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'nep_article',
                'permissions': [('edit_article', 'Can edit every article')],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NepArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('sort_num', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nep_article_category',
                'permissions': [('edit_article_category', 'Can edit every article category')],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NepArticleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='article_image')),
                ('linked_article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.neparticle')),
            ],
            options={
                'db_table': 'nep_article_image',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='neparticle',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.neparticlecategory'),
        ),
    ]
