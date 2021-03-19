import re
from ..models import NepArticle, NepArticleImage
import os


def optimize_article_image(article_id):
    print('optimize article image')
    img_list = NepArticleImage.objects.filter(linked_article=article_id)
    article_content = NepArticle.objects.get(pk=article_id).content
    if len(img_list) == 0:
        print('no image')
        return
    for each_img in img_list:
        if re.findall(each_img.image.url, article_content):
            print('find ', each_img.image.url)
        else:
            print('can not find', each_img.image.url)
            each_img.delete()


def get_art_list(page, limit):
    article_list = NepArticle.objects.all().order_by('id')[(page - 1) * limit: page * limit]
    art_list = []

    for each in article_list:
        art_list.append({
            'id': each.id,
            'title': each.title,
            'subtitle': each.subtitle,
            'create_time': each.create_time,
            'update_time': each.update_time,
            'view_time': each.view_time,
            'category': each.category.name if each.category else 'None',
            'auth': each.auth.username
        })

    return art_list
