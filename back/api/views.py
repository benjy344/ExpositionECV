from django.core import serializers
from django.core.exceptions import FieldDoesNotExist
from django.http import Http404, HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Page, Content, artwork, Place, Room, Author, Like
from .utils import to_json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def getallartworks(request):
    try:
        arts = artwork.objects.all()
        json = to_json(arts, request.path)
    except arts.DoesNotExist:
        json = to_json([], request.path, 'Artworks not found...', '')
    return JsonResponse(json, safe=False)


def getartwork(request, pk):
    try:
        artwork = artwork.objects.filter(id=pk)
        json = to_json(artwork, request.path)
    except artwork.DoesNotExist:
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


def getartworkbyroom(request, pk):
    try:
        artworks = artwork.objects.filter(room=pk)
        json = to_json(artworks, request.path)
    except artwork.DoesNotExist:
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
        json = to_json([], request.path, 'Page not found', '404')
    except Content.DoesNotExist:
        json = to_json([], request.path, 'Content not found', '404')
    return JsonResponse(json, safe=False)


def getallartworkbyparams(request):
    json = {}
    if request.method == 'GET':
        try:
            param = list(request.GET.keys())[0]
            artwork._meta.get_field(param)
            arts = artwork.objects.filter(** {param: request.GET.get(param)})
            json = to_json(arts, request.path)
        except artwork.DoesNotExist:
            json = to_json([], request.path, 'artwork not found', '404')
        except FieldDoesNotExist:
            json = to_json([], request.path, 'Field not exist', '500')
    else:
        json = to_json([], request.path, 'Bad method please use GET', '400')
    return JsonResponse(json, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
def addlike(request, pk):
    if request.method == 'POST':
        try:
            token = request.POST.get("token")
            art = artwork.objects.filter(id=pk)
            like = Like.objects.filter(token=token).filter(artwork=pk)
            if like:
                json = to_json([], request.path, 'Already liked', '500')
            else:
                newlike = Like(token=token, artwork=art[0])
                newlike.save()
                json = {'results': 'OK',
                        'error': {
                            'errorMessage': '',
                            'statusCode': ''
                        },
                        'url': ''}
        except artwork.DoesNotExist:
            json = to_json([], request.path, 'Artwork not found', '404')
    else:
        json = to_json([], request.path, 'Bad method please use POST', '400')
    return JsonResponse(json, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
def removelike(request, pk):
    if request.method == 'POST':
        try:
            token = request.POST.get("token")
            art = artwork.objects.filter(id=pk)
            like = Like.objects.filter(token=token).filter(artwork=pk)
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
        except artwork.DoesNotExist:
            json = to_json([], request.path, 'Artwork not found', '404')
    else:
        json = to_json([], request.path, 'Bad method please use POST', '400')
    return JsonResponse(json, safe=False)
