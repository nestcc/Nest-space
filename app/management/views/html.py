from django.shortcuts import render
from django.contrib.auth.decorators import permission_required


# Create your views here.
@permission_required('user.view_nepuser', 'article.view_neparticle', raise_exception=True)
def index(request):
    return render(request, 'management/management.html')
