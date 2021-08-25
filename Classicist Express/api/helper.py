def converter(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


def appender(lis, i):
    lis.append(i.heading)
    lis.append(i.news)
    lis.append(i.tags)
    lis.append(str(i.picture))
