from django.contrib.auth import logout
from django.http.response import HttpResponseRedirect
from ..models import NepDiskFile


def empty_redirect(request):
    return HttpResponseRedirect('/disk/home/')


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/disk/home/')


def del_file(request, file_id):
    try:
        file = NepDiskFile.objects.get(id=file_id)
        print(request.user.id, file.owner.id)
        if file.owner.id == request.user.id:
            file.delete()
        return HttpResponseRedirect('/disk/my_home/')
    except Exception as any_exec:
        return HttpResponseRedirect('/disk/my_home/')