def converter(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


def appender(send_api, i, n):
    send_api['heading'][n] = i.heading
    send_api['news'][n] = i.news
    send_api['tags'][n] = i.tags
    send_api['picture'][n] = str(i.picture)
    send_api['link'][n] = i.id
    return send_api
