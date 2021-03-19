'''
Author: Nestcc
Date: 2020-08-10 10:40:04
LastEditors: Nestcc
LastEditTime: 2021-03-19 13:51:49
Description:  < file content > 
'''
from django.shortcuts import render
from disk.models import NepDiskFile
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
import random, string
from django.http.response import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect


# Create your views here.
class Home(TemplateView):
    template_name = 'disk/base.html'


class MyHome(LoginRequiredMixin, View):
    login_url = '/admin/login/'

    def get(self, request):
        print(request.user)
        files = NepDiskFile.objects.filter(owner=request.user)

        return render(request, 'disk/my_content.html', {'content': files, 'host': request.get_host()})

    def post(self, request):
        if request.FILES:
            try:
                code = ''.join(random.sample(string.digits, 10))
                for each in request.FILES.getlist('file'):
                    NepDiskFile.objects.create(
                        file=each,
                        name_display=each.name,
                        code=code,
                        owner=request.user,
                        upload_ip=request.META['REMOTE_ADDR']
                    )
                return HttpResponsePermanentRedirect("/disk/s/" + code)

            except Exception as any_exec:
                print(repr(any_exec))
                return HttpResponseRedirect("/disk/home/")
        else :
            return HttpResponse("not file")


class Display(View):

    @transaction.atomic
    def get(self, request, code):

        files = NepDiskFile.objects.filter(code=code)
        for each in files:
            each.total_count += 1
            each.save()
        return render(request, 'disk/content.html', {'content': files, 'host': request.get_host()})
