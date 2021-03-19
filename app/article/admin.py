from django.contrib import admin
from django.utils.timezone import now

from .models import NepArticle, NepArticleCategory


# Register your models here. #


class ArticleAdmin(admin.ModelAdmin):
    fields = ('title',
              'subtitle',
              'content',
              'key_words',
              'category',
              'is_original',
              'link',
              'cover_image',
              'auth')

    list_display = ('title',
                    'create_time',
                    'update_time',
                    'key_words',
                    'category',
                    'auth')

    def save_model(self, request, obj, form, change):
        obj.auth = request.user
        obj.update_time = now()
        super(ArticleAdmin, self).save_model(request, obj, form, change)


admin.site.register(NepArticle, ArticleAdmin)

admin.site.register(NepArticleCategory)
