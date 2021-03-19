from django.urls import path
from .views.html import *
from .views.redirect import *

paths = [
    path('', empty_redirect),
    path('logout/', log_out),
    path('home/', Home.as_view(), name='home'),

    path('my_home/', MyHome.as_view(), name='my_home'),
    path('s/<code>/', Display.as_view()),
    path('delete/<int:file_id>/', del_file)
]