"""netdisk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user.urls import paths as user_path
from management.urls import paths as mana_path
from article.urls import paths as art_path
from disk.urls import paths as disk_path
from blog.urls import paths as blog_path
from blog.views.html import empty_redirect

# url分发到各个app中
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(blog_path)),
    # path('user/', include(user_path)),
    # path('mana/', include(mana_path)),
    # path('article/', include(art_path)),
    path('', empty_redirect),
    path('disk/', include(disk_path)),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]
