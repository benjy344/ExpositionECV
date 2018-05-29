from django.http import JsonResponse


# Fonction pour faire un json à partir d'une queryset ou d'une erreur
def to_json(queryset, url='', err='', errcode=''):
    json = {'results': [],
            'error': {
                'errorMessage': '',
                'statusCode': ''
            },
            'url': ''}
    for result in queryset:
        temp = result.__dict__
        temp['_state'] = ""
        json['results'].append(temp)
    if err and errcode:
        json['error']['errorMessage'] = err
        json['error']['statusCode'] = errcode
    if url:
        json['url'] = url
    return json


# Focntion pour crée le header de retour par défaut get (80% des routes)
def request_return(json, method='GET'):
    response = JsonResponse(json, safe=False)
    response["Access-Control-Allow-Origin"] = "localhost"
    response["Access-Control-Allow-Methods"] = ""+method
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    response['Cache-Control'] = 'max-age=10000'
    return response
