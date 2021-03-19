from django.http import JsonResponse
from ..models import NepArticleImage, NepArticle
from django.contrib.auth.decorators import permission_required
from ..controller.article_handler import get_art_list


@permission_required('article.edit_article')
def upload_article_image(request):
    new_img = NepArticleImage()
    print(request.POST)
    print(request.FILES)
    new_img.image = request.FILES['image']
    try:
        new_img.save()
        print(new_img.id)
        return JsonResponse({'status': 'success',
                             'location': '/static/media/'+new_img.image.url,
                             'file_id': str(new_img.id)})
    except Exception as any_exec:
        return JsonResponse({'status': 'fail',
                             'error': repr(any_exec)})


@permission_required('article.edit_article')
def get_article_list(request):
    art_list = get_art_list(int(request.GET['page']), int(request.GET['limit']))
    return JsonResponse({
        'code': 0,
        'msg': '',
        'count': NepArticle.objects.all().count(),
        'data': art_list
    })


@permission_required('article.edit_article', raise_exception=True)
def delete_article(request, article_id):

    article = NepArticle.objects.get(id=article_id)
    try:
        article.delete()
        return JsonResponse({'status': 'success'})
    except Exception as any_exec:
        return JsonResponse({'status': 'fail',
                             'error': repr(any_exec)})
