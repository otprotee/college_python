from django.http import HttpResponse
from django.template import loader


def members(request):
    return HttpResponse('hello world')