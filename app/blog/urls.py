from django.urls import path
from .views.html import *


paths = [
    # path('', empty_redirect),
    path('home/', Index.as_view()),

    path('article_list/<int:page>/', ArticleList.as_view()),
    path('article/<int:arti_id>/', ArticlePage.as_view())
]