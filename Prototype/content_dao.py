from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Item(db.Model):
    __tablename__ = 'content'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(20))
    platform = db.Column(db.String(10))
    type = db.Column(db.String(10))
    image_url = db.Column(db.String(100))
    video_url = db.Column(db.String(100))


class AllowedItem(db.Model):
    __tablename__ = 'access_list'
    id = db.Column(db.Integer(), primary_key=True)

    def __init__(self, item_id):
        self.id = item_id


def query_platform(platform):
    query_result = db.session.query(Item).filter(Item.platform == platform)
    movie_list = []
    series_list = []
    for item in query_result:
        if item.type == 'movie':
            movie_list.append({'id': item.id, 'title': item.title, 'image_url': item.image_url})
        else:
            series_list.append({'id': item.id, 'title': item.title, 'image_url': item.image_url})

    result_dict = {'movies': movie_list, 'series': series_list}
    return result_dict


def query_id(item_id):
    query_result = db.session.query(Item).get(item_id)
    result_dict = {'id': query_result.id, 'title': query_result.title, 'image_url': query_result.image_url,
                   'video_url': query_result.video_url}
    return result_dict


def check_access(item_id):
    query_result = db.session.query(AllowedItem).filter(AllowedItem.id == item_id).first()
    if query_result is None:
        return False
    return True


def grant_access(item_id):
    allowed_item = AllowedItem(item_id)
    db.session.add(allowed_item)
    db.session.commit()
