from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from django.views.decorators.clickjacking import xframe_options_exempt
from ..models import NepArticle, NepArticleImage
from ..controller.article_handler import optimize_article_image


# """
# 添加文章类
# """
class CreateArtView(PermissionRequiredMixin, View):
    permission_required = 'article.edit_article'
    raise_exception = True

    @xframe_options_exempt
    def get(self, request):
        print(request.user.get_all_permissions())
        return render(request, 'article/create_article.html')

    def post(self, request):
        print(request.POST)
        try:
            new_article = NepArticle.objects.create(
                title=request.POST['title'],
                auth=request.user,
                subtitle=request.POST['subtitle'],
                content=request.POST['content']
            )
            print(new_article.id, new_article.title, new_article.subtitle)
            optimize_article_image(new_article.id)
            return JsonResponse({'status': 'success'})
        except Exception as any_exec:
            return JsonResponse({'status': 'fail',
                                 'error': repr(any_exec)})


# """
# 文章列表类
# """
class ArticleList(PermissionRequiredMixin, View):
    permission_required = 'article.edit_article'
    raise_exception = True

    @xframe_options_exempt
    def get(self, request):
        return render(request, 'article/article_list.html')

    def post(self, request):
        return JsonResponse({})

