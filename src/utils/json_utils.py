from urllib.parse import unquote

def to_dict(data):
    rs = {}
    for attr in data.split('&'):
        temp = attr.split('=')
        rs[unquote(unquote(str(temp[0])))] = str(unquote(unquote(temp[1])))

    return rs
