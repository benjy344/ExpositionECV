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

