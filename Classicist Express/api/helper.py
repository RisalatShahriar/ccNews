import json


def appender(send_api, i, n):
    send_api['heading'][n] = i.heading
    send_api['news'][n] = i.news
    send_api['tags'][n] = i.tags
    send_api['picture'][n] = str(i.picture)
    send_api['link'][n] = i.id
    return send_api


def api_send(news):
    send_api = {
        'heading': {},
        'news': {},
        'tags': {},
        'picture': {},
        'link': {}
    }
    count = 1
    for i in news:
        appender(send_api, i, count)
        count += 1
    return json.dumps(send_api)
