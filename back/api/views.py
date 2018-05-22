from django.core import serializers
from django.http import Http404, HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Page, Content, Artwortk, Place, Room, Author, Like


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def getallartwortks(request):
    try:
        artwortk = Artwortk.objects.all()
        artwortk_serialized = [ i.__dict__ for i in artwortk]
        for e in artwortk_serialized:
            e['_state'] = ""
    except Artwortk.DoesNotExist:
        raise Http404
    return JsonResponse({'result': artwortk_serialized}, safe=False)


def getartwortk(request,pk):
    try:
        artwortk = Artwortk.objects.filter(id=pk)
        artwortk_serialized = serializers.serialize('json', artwortk)
    except Artwortk.DoesNotExist:
        raise Http404
    return JsonResponse(artwortk_serialized, safe=False)


def getallplaces(request):
    try:
        place = Place.objects.all()
        place_serialized = serializers.serialize('json', place)
    except Place.DoesNotExist:
        raise Http404
    return JsonResponse(place_serialized, safe=False)


def getplace(request,pk):
    try:
        place = Place.objects.filter(id=pk)
        place_serialized = serializers.serialize('json', place)
    except Place.DoesNotExist:
        raise Http404
    return JsonResponse(place_serialized, safe=False)


def getplacemap(request,pk):
    try:
        content_list = []
        pages = Page.objects.filter(place=pk)
        for page in pages :
            content = Content.objects.filter(page=page.id)
            if content[0].type == 'map':
                content_list.append(serializers.serialize('json', content))
    except Page.DoesNotExist:
        raise Http404
    except Content.DoesNotExist:
        raise Http404
    return JsonResponse(content_list, safe=False)


def getallroomsbyplace(request,pk):
    try:
        rooms = Room.objects.filter(place=pk)
        rooms = serializers.serialize('json', rooms)
    except Room.DoesNotExist:
        raise Http404
    return JsonResponse(rooms, safe=False)


def getroom(request,pk):
    try:
        rooms = Room.objects.filter(id=pk)
        rooms = serializers.serialize('json', rooms)
    except Room.DoesNotExist:
        raise Http404
    return JsonResponse(rooms, safe=False)


def getartwortkbyroom(request,pk):
    try:
        artwortks = Artwortk.objects.filter(room=pk)
        artwortks = serializers.serialize('json', artwortks)
    except Artwortk.DoesNotExist:
        raise Http404
    return JsonResponse({'ae':artwortks}, safe=False)


def getpageplace(request,pk):
    try:
        content_list = []
        pages = Page.objects.filter(place=pk)
        for page in pages:
            content = Content.objects.filter(page=page.id)
            content_list.append(serializers.serialize('json', content))
    except Page.DoesNotExist:
        raise Http404
    except Content.DoesNotExist:
        raise Http404
    return JsonResponse(content_list, safe=False)


def getpageplaceinfos(request,pk):
    try:
        content_list = []
        pages = Page.objects.filter(place=pk).filter(name="Infos pratiques")
        for page in pages:
            content = Content.objects.filter(page=page.id).filter(page=2)
            content_list.append(serializers.serialize('json', content))
    except Page.DoesNotExist:
        raise Http404
    except Content.DoesNotExist:
        raise Http404
    return JsonResponse(content_list, safe=False)


def getpageplacehome(request,pk):
    try:
        content_list = []
        pages = Page.objects.filter(place=pk).filter(name="Home")
        for page in pages:
            content = Content.objects.filter(page=page.id)
            content_list.append(serializers.serialize('json', content))
    except Page.DoesNotExist:
        raise Http404
    except Content.DoesNotExist:
        raise Http404
    return JsonResponse(content_list, safe=False)


def getallartwortkbyparams(request):
    arts = []
    if request.method == 'GET':
        try:
            param = request.GET.get("param")
            value = request.GET.get("value")
            if param == "author":
                arts = Artwortk.objects.filter(author=value)
                arts = serializers.serialize('json', arts)
            elif param == "name":
                arts = Artwortk.objects.filter(name=value)
                arts = serializers.serialize('json', arts)
            elif param == "room":
                arts = Artwortk.objects.filter(room=value)
                arts = serializers.serialize('json', arts)
        except Artwortk.DoesNotExist:
            raise Http404
    else:
        raise Http404
    return JsonResponse(arts, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
def addlike(request,pk):
    if request.method == 'POST':
        try:
            token = request.POST.get("token")
            art = Artwortk.objects.filter(id=pk)

            like = Like.objects.filter(token=token).filter(artwortk=pk)
            if like:
                raise Http404
            else:
                newlike = Like(token=token, artwortk=art[0])
                newlike.save()
        except Artwortk.DoesNotExist:
            raise Http404
    else:
        raise Http404
    return JsonResponse("OK", safe=False)


@method_decorator(csrf_exempt, name='dispatch')
def removelike(request,pk):
    if request.method == 'POST':
        try:
            token = request.POST.get("token")
            art = Artwortk.objects.filter(id=pk)

            like = Like.objects.filter(token=token).filter(artwortk=pk)
            if like:
                like.delete()
            else:
                raise Http404
        except Artwortk.DoesNotExist:
            raise Http404
    else:
        raise Http404
    return JsonResponse("OK", safe=False)