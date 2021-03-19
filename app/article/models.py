from ckeditor.fields import RichTextField
from django.db import models
from django.utils.timezone import now

from user.models import NepUser


class NepArticleCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    sort_num = models.IntegerField(default=0)  # 排列顺序
    description = models.CharField(max_length=100, null=True, blank=True)  # 描述

    class Meta:
        managed = True
        db_table = 'nep_article_category'
        permissions = [('edit_article_category', 'Can edit every article category')]


class NepArticle(models.Model):
    title = models.CharField(max_length=50, default="None Title")
    subtitle = models.CharField(max_length=100, null=True, blank=True)  # 副标题
    create_time = models.DateTimeField(null=True, default=now)  # 创建日期
    update_time = models.DateTimeField(null=True)  # 更新日期
    view_time = models.IntegerField(default=0)  # 查看次数
    content = RichTextField(null=True)  # 内容
    key_words = models.CharField(max_length=100, null=True, blank=True)  # 文章关键字
    category = models.ForeignKey(NepArticleCategory, on_delete=models.SET_NULL, null=True, blank=True)  # 文章分类
    is_original = models.BooleanField(default=True)  # 是否原创
    link = models.CharField(max_length=100, null=True, blank=True)  # 原文链接
    cover_image = models.ImageField(null=True, upload_to='article_image', blank=True,
                                    default='article_image/default_cover.jpg')  # 封面图片
    auth = models.ForeignKey(NepUser, on_delete=models.CASCADE)  # 作者

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     self.update_time = now()
    #     super(NepArticle, self).save()

    class Meta:
        managed = True
        db_table = 'nep_article'
        permissions = [('edit_article', 'Can edit every article')]


class NepArticleImage(models.Model):
    image = models.ImageField(null=False, upload_to='article_image')  # 图片
    linked_article = models.ForeignKey(NepArticle, null=True, on_delete=models.CASCADE)  # 所属文章

    class Meta:
        managed = True
        db_table = 'nep_article_image'

    def delete(self, using=None, keep_parents=False):
        storage, path = self.image.storage, self.image.path
        storage.delete(path)
        super(NepArticleImage, self).delete()
