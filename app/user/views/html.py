"""
用于用户相关操作的views
"""

from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponseRedirect, JsonResponse
from ..controller.user_handler import *


def login(request):
    print(request.user.id)
    if request.user.id is not None:
        return HttpResponseRedirect('/mana/index/')
    else:
        return render(request, 'index/login.html')


class UserList(PermissionRequiredMixin, View):
    permission_required = ('user.view_nepuser', 'user.change_nepuser')

    @xframe_options_exempt
    def get(self, request):
        return render(request, 'user/user_list.html')


class UserDetail(PermissionRequiredMixin, View):
    permission_required = ('user.view_nepuser', 'user.change_nepuser')

    @xframe_options_exempt
    def get(self, request, user_id):
        return render(request, 'user/user_detail_tab.html', {'user': NepUser.objects.get(pk=user_id)})

    def post(self, request, user_id):
        return JsonResponse(handle_change_user_info(request, user_id))


class AddUser(PermissionRequiredMixin, View):
    permission_required = ('user.view_nepuser', 'user.change_nepuser')

    @xframe_options_exempt
    def get(self, request):
        return render(request, 'user/add_user_tab.html')

    def post(self, request):
        return JsonResponse(handle_add_user(request.POST))


class delet_user(PermissionRequiredMixin, View):
    permission_required = ('user.view_nepuser', 'user.delet_nepuser')

    def get(self, request):
        return

    def post(self, request):
        print(request.POST)
        return JsonResponse(handle_del_user(request.POST['user_id']))