from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest
from django.http import HttpResponse


def index(request):

    # return HttpResponse('ok')
    # 100/0
    context={
        'name':'马上双十一,66622'
    }

    return render(request,'book/index.html',context=context)