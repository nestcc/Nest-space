from django.views.generic import View, TemplateView
from django.shortcuts import render
from user.models import NepUser
from article.models import NepArticle
from django.http.response import HttpResponse, HttpResponseRedirect


def empty_redirect(request):
    return HttpResponseRedirect('/blog/home/')


class Index(View):

    template_name = "blog/blogs.html"

    def get(self, request):
        # limit, page = request.GET['limit'], request.GET['page']
        articles = NepArticle.objects.all()[0:5]
        count = NepArticle.objects.count()

        return render(request, 'blog/blogs.html', {'articles': articles,
                                                   'article': 'class=active',
                                                   'count': count,
                                                   'curr': 1})


class ArticleList(View):
    def get(self, request, page=1):
        articles = NepArticle.objects.all()[(page - 1) * 5: page * 5]
        count = NepArticle.objects.count()

        return render(request, 'blog/blogs.html', {'articles': articles,
                                                   'article': 'class=active',
                                                   'count': count,
                                                   'curr': page})


class ArticlePage(View):
    def get(self, request, arti_id):
        article = NepArticle.objects.get(id=arti_id)

        return render(request, 'blog/blog_page.html', {'content': article,
                                                       'article': 'class=active'})

