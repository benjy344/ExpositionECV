from django.core import serializers
from django.http import Http404, HttpResponse, JsonResponse

from .models import Place, Page, Content


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def getpageplace(request,pk):
    try:
        content_list = []
        pages = Page.objects.filter(place=pk)
        for page in pages   :
            content = Content.objects.filter(page=page.id)
            content_list.append(serializers.serialize('json', content))
    except Page.DoesNotExist:
        raise Http404
    except Content.DoesNotExist:
        raise Http404
    return JsonResponse(content_list,safe=False)