from bson.objectid import ObjectId


def make_query(id: str = None, color: str = None, **kwargs):
    query = {}
    if id:
        query['_id'] = ObjectId(id)
    if color:
        query['color'] = color

    return query
