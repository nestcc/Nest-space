from django.contrib.auth import logout
from django.http.response import HttpResponseRedirect


def empty_redirect(request):
    return HttpResponseRedirect('/blog/home/')
