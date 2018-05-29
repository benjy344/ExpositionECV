from django.core.exceptions import FieldDoesNotExist
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Page, Content, Artwork, Place, Room, Author, Like
from .utils import to_json, request_return


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# Recupère tous les object de la classe Artwork
def getallartworks(request):
    try:
        arts = Artwork.objects.all()
        json = to_json(arts, request.path)
    except Artwork.DoesNotExist:
        json = to_json([], request.path, 'Artworks not found...', '')
    return request_return(json)


# Recupère tous les object de la classe Artwork qui ont l'id PK
def getartwork(request, pk):
    try:
        art = Artwork.objects.filter(id=pk)
        json = to_json(art, request.path)
    except Artwork.DoesNotExist:
        json = to_json([], request.path, 'Artwork not found', '')
    return request_return(json)


# Recupère tous les object de la classe Place
def getallplaces(request):
    try:
        places = Place.objects.all()
        json = to_json(places, request.path)
    except Place.DoesNotExist:
        json = to_json([], request.path, 'Place not found', '')
    return request_return(json)


def getplace(request, pk):
    try:
        place = Place.objects.filter(id=pk)
    except Place.DoesNotExist:
        json = to_json([], request.path, 'Place not found', '')
    return request_return(json)


# Recupère la map d'une page qui est dans la table contenue (clé étrangère sur l'id de la pages)
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
    return request_return(json)


def getallroomsbyplace(request, pk):
    try:
        rooms = Room.objects.filter(place=pk)
        json = to_json(rooms, request.path)
    except Room.DoesNotExist:
        json = to_json([], request.path, 'Rooms not found', '')
    return request_return(json)


def getroom(request, pk):
    try:
        rooms = Room.objects.filter(id=pk)
        json = to_json(rooms, request.path)
    except Room.DoesNotExist:
        json = to_json([], request.path, 'Rooms not found', '')
    return request_return(json)


# Récuprere les oeuvres qui sont dans la salle avec l'id pk
def getartworkbyroom(request, pk):
    try:
        artworks = Artwork.objects.filter(room=pk)
        json = to_json(artworks, request.path)
    except Artwork.DoesNotExist:
        json = to_json([], request.path, 'Artworks not found', '')
    return request_return(json)


# Récuprere les contenue pour les pages d'une exposition (pk est l'id de l'exposition(place))
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
    return request_return(json)


# idem que audessus mais pour avoir seulement la page infos pratique
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
    return request_return(json)

# idem que audessus mais pour avoir seulement la page home
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
    return request_return(json)


# Permet de faire une recherche par rapport à un attribu de la table artwork sous la forme d'une URL
# /api/artworks/search?name=Safe%20Place
def getallartworkbyparams(request):
    json = {}
    if request.method == 'GET':
        try:
            param = list(request.GET.keys())[0]
            Artwork._meta.get_field(param)
            arts = Artwork.objects.filter(** {param: request.GET.get(param)})
            json = to_json(arts, request.path)
        except Artwork.DoesNotExist:
            json = to_json([], request.path, 'artwork not found', '404')
        except FieldDoesNotExist:
            json = to_json([], request.path, 'Field not exist', '500')
    else:
        json = to_json([], request.path, 'Bad method please use GET', '400')
    return request_return(json)


# method POST pour ajouter un like à une image avec un token passé via HTTP_AUTHORIZATION
# le décorateur permet de ne pas avoir la validation de token crsf de django
@method_decorator(csrf_exempt, name='dispatch')
def addlike(request, pk):
    if request.method == 'POST':
        try:
            token = request.META.get('HTTP_AUTHORIZATION')
            if token is None:
                json = to_json([], request.path, 'Bad Token', '500')
                return request_return(json)
            art = Artwork.objects.filter(id=pk)
            like = Like.objects.filter(token=token).filter(artwork=pk)
            if like:
                json = to_json([], request.path, 'Already liked', '500')
            else:
                if art:
                    newlike = Like(token=token, artwork=art[0])
                    newlike.save()
                    json = {'results': 'OK',
                            'error': {
                                'errorMessage': '',
                                'statusCode': ''
                            },
                            'url': ''}
        except Artwork.DoesNotExist:
            json = to_json([], request.path, 'Artwork not found', '404')
    else:
        json = to_json([], request.path, 'Bad method please use POST', '400')
    return request_return(json, 'POST')


# method POST pour retirer un like à une image avec un token passé via HTTP_AUTHORIZATION
# le décorateur permet de ne pas avoir la validation de token crsf de django
@method_decorator(csrf_exempt, name='dispatch')
def removelike(request, pk):
    if request.method == 'POST':
        try:
            token = request.META.get('HTTP_AUTHORIZATION')
            if token is None:
                json = to_json([], request.path, 'Bad Token', '500')
                return request_return(json)
            art = Artwork.objects.filter(id=pk)
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
        except Artwork.DoesNotExist:
            json = to_json([], request.path, 'Artwork not found', '404')
    else:
        json = to_json([], request.path, 'Bad method please use POST', '400')
    return request_return(json, 'POST')


def getlikesbyartwork(request, pk):
    try:
        likes = Like.objects.filter(artwork=pk)
        json = to_json(likes, request.path)
    except Like.DoesNotExist:
        json = to_json([], request.path, 'Like not found', '404')
    return request_return(json)


def getlikesbytoken(request):
    try:
        t = request.META.get('HTTP_AUTHORIZATION')
        likes = Like.objects.filter(token=t)
        json = to_json(likes, request.path)
    except Like.DoesNotExist:
        json = to_json([], request.path, 'Like not found', '404')
    return request_return(json)


def getauthor(request, pk):
    try:
        art = Author.objects.filter(id=pk)
        json = to_json(art, request.path)
    except Author.DoesNotExist:
        json = to_json([], request.path, 'Artwork not found', '')
    return request_return(json)


def getallauthor(request):
    try:
        art = Author.objects.all()
        json = to_json(art, request.path)
    except Author.DoesNotExist:
        json = to_json([], request.path, 'Artwork not found', '')
    return request_return(json)