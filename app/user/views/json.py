"""
用于用户相关操作的views
"""

from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate, login, logout
from ..controller.user_handler import *


#
def register(request):
    print(request.POST)
    try:
        NepUser.objects.create_user(username=request.POST['user_name'],
                                    password=request.POST['password'],
                                    mobile=request.POST['mobile'])
        return JsonResponse({'status': 'success'})
    except Exception as exec:
        return JsonResponse({'status': 'fail',
                             'error': repr(exec)})


def log_out(request):
    print('logout: ', request.user.username)
    print(request.META.get('HTTP_REFERER', '/'))
    try:
        logout(request)
        return JsonResponse({'status': 'success'})
    except Exception as any_exec:
        return JsonResponse({'status': 'fail',
                             'error': repr(any_exec)})


def log_in(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    print('request: ', request.POST)
    user = authenticate(request,
                        username=request.POST['username'],
                        password=request.POST['password'])
    if user:
        login(request, user)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'fail',
                             'error': 'wrong message'})


@permission_required('user.view_nepuser')
def get_user_list(request):
    page, limit = int(request.GET['page']), int(request.GET['limit'])
    user_list = get_ulist_with_var(page, limit, 'normal_user')
    return JsonResponse({
        'code': 0,
        'msg': '',
        'count': NepUser.objects.filter(groups__name__contains='normal_user').count(),
        'data': user_list
    })


@permission_required('user.change_nepuser')
def upload_user_icon(request, user_id):
    # print(re)
    return JsonResponse(handle_upload_user_icon(request.FILES['file'], user_id))


@permission_required('user.change_nepuser')
def change_user_info(request, user_id):
    return JsonResponse(handle_change_user_info(request, user_id))


@permission_required('user.change_nepuser')
def change_user_pwd(request, user_id):
    return JsonResponse(handle_change_pwd(user_id, request.POST['pwd']))


