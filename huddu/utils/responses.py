import json


class Str(str):
    pass


class Dict(str):
    pass


class List(str):
    pass


def make_response(items):
    res = []
    for item in items:
        item_data = item["data"]

        try:
            item_data = json.loads(item_data)
        except:
            ...

        formatted = None
        if type(item_data) == str:
            formatted = Str(item["data"])
            try:
                formatted.size = item["size"]
                formatted.total_size = item["total_size"]

                formatted.content_type = item["content_type"]
                formatted.created = item["created"]
                formatted.updated = item["updated"]
            except:
                pass

        elif type(item_data) == dict:
            formatted = Dict(item["data"])
            try:
                formatted.size = item["size"]
                formatted.total_size = item["total_size"]

                formatted.content_type = item["content_type"]
                formatted.created = item["created"]
                formatted.updated = item["updated"]
            except:
                pass

        elif type(item_data) == list:
            formatted = List(item["data"])
            try:
                formatted.size = item["size"]
                formatted.total_size = item["total_size"]

                formatted.content_type = item["content_type"]
                formatted.created = item["created"]
                formatted.updated = item["updated"]
            except:
                pass
        if formatted:
            res.append(formatted)

    return res
