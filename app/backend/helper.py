import json

def json_data(url, msg, code=1):
    data = {
        'code' : code,
        'msg' : msg,
        'url' : url,
        'wait' : 3
    }
    return json.dumps(data)


def json_lists(lists, code=0, pri_key='id'):
    items = []
    for item in lists['list'] :
        row = row2dict(item)
        items.append(row)

    data = {
        'code' : code,
        'data' : items,
        'count' : lists['total']
    }
    return json.dumps(data)

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d
