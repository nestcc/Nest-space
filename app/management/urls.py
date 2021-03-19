from django.urls import path
from .views import html as mana_html

paths = [path('index/', mana_html.index),
        ]
