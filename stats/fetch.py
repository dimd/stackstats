from urlparse import urljoin

import requests
from dateutil.parser import parse

from config import API_URL, API_PARAMETERS


def get(resource, params={}):
    """Get a stackexchange resource.

    Due to pagination multiple calls to the API might be needed.
    """
    url = urljoin(API_URL, resource)
    params.update(API_PARAMETERS)
    items = []
    more = True
    page = 0

    print('Fetching data....')
    while more:
        page += 1
        params.update({'page': page})
        data = requests.get(url, params).json()
        more = data.get('has_more')
        for item in data.get('items'):
            items.append(item)

    return items


def get_answers(since, until):
    """Get stackoverflow answers."""
    params = {
        'fromdate': parse(since).strftime('%s'),
        'todate': parse(until).strftime('%s')
    }

    return get('answers', params)


def get_comment(answer_id):
    """Get stackoverflow comments of an answer."""
    return get('answers/{0}/comments'.format(answer_id))
