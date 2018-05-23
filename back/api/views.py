from django.core import serializers
from django.http import Http404, HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Page, Content, Artwortk, Place, Room, Author, Like
from .utils import to_json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def getallartwortks(request):
    try:
        artwortk = Artwortk.objects.all()
        json = to_json(artwortk, request.path)
    except Artwortk.DoesNotExist:
        json = to_json([], request.path, 'Artwork not found', '')
    return JsonResponse(json, safe=False)


def getartwortk(request, pk):
    try:
        artwortk = Artwortk.objects.filter(id=pk)
        json = to_json(artwortk, request.path)
    except Artwortk.DoesNotExist:
        json = to_json([], request.path, 'Artwork not found', '')
    return JsonResponse(json, safe=False)


def getallplaces(request):
    try:
        places = Place.objects.all()
        json = to_json(places, request.path)
    except Place.DoesNotExist:
        json = to_json([], request.path, 'Place not found', '')
    return JsonResponse(json, safe=False)


def getplace(request, pk):
    try:
        place = Place.objects.filter(id=pk)
    except Place.DoesNotExist:
        json = to_json([], request.path, 'Place not found', '')
    return JsonResponse(json, safe=False)


def getplacemap(request, pk):
    json = {}
    try:
        pages = Page.objects.filter(place=pk)
        for page in pages :
            content = Content.objects.filter(page=page.id)
            if content[0].type == 'map':
                json = to_json(content, request.path)
    except Page.DoesNotExist:
        json = to_json([], request.path, 'Page not found', '')
    except Content.DoesNotExist:
        json = to_json([], request.path, 'Content not found', '')
    return JsonResponse(json, safe=False)


def getallroomsbyplace(request, pk):
    try:
        rooms = Room.objects.filter(place=pk)
        json = to_json(rooms, request.path)
    except Room.DoesNotExist:
        json = to_json([], request.path, 'Rooms not found', '')
    return JsonResponse(json, safe=False)


def getroom(request, pk):
    try:
        rooms = Room.objects.filter(id=pk)
        json = to_json(rooms, request.path)
    except Room.DoesNotExist:
        json = to_json([], request.path, 'Rooms not found', '')
    return JsonResponse(json, safe=False)


def getartwortkbyroom(request, pk):
    try:
        artwortks = Artwortk.objects.filter(room=pk)
        json = to_json(artwortks, request.path)
    except Artwortk.DoesNotExist:
        json = to_json([], request.path, 'Artworks not found', '')
    return JsonResponse(json, safe=False)


def getpageplace(request, pk):
    json = {}
    try:
        pages = Page.objects.filter(place=pk)
        for page in pages:
            content = Content.objects.filter(page=page.id)
            json = to_json(content, request.path)
    except Page.DoesNotExist:
        json = to_json([], request.path, 'Page not found', '')
    except Content.DoesNotExist:
        json = to_json([], request.path, 'Content not found', '')
    return JsonResponse(json, safe=False)


def getpageplaceinfos(request, pk):
    json = {}
    try:
        pages = Page.objects.filter(place=pk).filter(name="Infos pratiques")
        for page in pages:
            content = Content.objects.filter(page=page.id).filter(page=2)
            json = to_json(content, request.path)
    except Page.DoesNotExist:
        json = to_json([], request.path, 'Page not found', '')
    except Content.DoesNotExist:
        json = to_json([], request.path, 'Content not found', '')
    return JsonResponse(json, safe=False)


def getpageplacehome(request, pk):
    json = {}
    try:
        pages = Page.objects.filter(place=pk).filter(name="Home")
        for page in pages:
            content = Content.objects.filter(page=page.id)
            json = to_json(content, request.path)
    except Page.DoesNotExist:
        json = to_json([], request.path, 'Page not found', '')
    except Content.DoesNotExist:
        json = to_json([], request.path, 'Page not found', '')
    return JsonResponse(json, safe=False)


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
def addlike(request, pk):
    if request.method == 'POST':
        try:
            token = request.POST.get("token")
            art = Artwortk.objects.filter(id=pk)

            like = Like.objects.filter(token=token).filter(artwortk=pk)
            if like:
                json = to_json([], request.path, 'Already liked', '500')
            else:
                newlike = Like(token=token, artwortk=art[0])
                newlike.save()
                json = {'results': 'OK',
                        'error': {
                            'errorMessage': '',
                            'statusCode': ''
                        },
                        'url': ''}
        except Artwortk.DoesNotExist:
            json = to_json([], request.path, 'Artwork not found', '404')
    else:
        json = to_json([], request.path, 'Bad method please use POST', '400')
    return JsonResponse(json, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
def removelike(request, pk):
    if request.method == 'POST':
        try:
            token = request.POST.get("token")
            art = Artwortk.objects.filter(id=pk)
            like = Like.objects.filter(token=token).filter(artwortk=pk)
            if like:
                like.delete()
                json = {'results': 'OK',
                        'error': {
                            'errorMessage': '',
                            'statusCode': ''
                        },
                        'url': ''}
            else:
                json = to_json([], request.path, 'Like not found', '404')
        except Artwortk.DoesNotExist:
            json = to_json([], request.path, 'Artwork not found', '404')
    else:
        json = to_json([], request.path, 'Bad method please use POST', '400')
    return JsonResponse(json, safe=False)