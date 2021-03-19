from django.urls import path
from .views import html as art_html
from .views import json as art_json

paths = [path('create_article/', art_html.CreateArtView.as_view(), name='create_article'),
         path('article_list/', art_html.ArticleList.as_view(), name='article_list'),

         path('upload_article_image/', art_json.upload_article_image),
         path('get_article_list/', art_json.get_article_list),
         path('del_article/<int:article_id>/', art_json.delete_article)
         ]
