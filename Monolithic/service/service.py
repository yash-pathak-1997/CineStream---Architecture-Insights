import json
from dao.dao import get_user_dao, create_user_dao, get_contents_dao, get_providers_dao
from dao.dao import create_provider_dao, create_content_dao, get_user_content_dao, user_subscribe_dao


def get_user_service(username, password):
    user = get_user_dao(username)
    print(user)
    if user and user['password'] == password:
        return True
    return False


def create_user_service(username, password, email):
    res = create_user_dao(username, password, email)
    return res


def get_content_service():
    contents = get_contents_dao()
    return contents


def create_content_service(id, name, des, srate, provider):
    res = create_content_dao(id, name, des, srate, provider)
    return res


def get_provider_service():
    providers = get_providers_dao()
    return providers


def create_provider_service(provider_name, srate):
    res = create_provider_dao(provider_name, srate)
    return res


def get_user_content_service(user_email):
    res = get_user_content_dao(user_email)
    return res


def user_subscribe_service(user_email, content_id):
    res = user_subscribe_dao(user_email, content_id)
    return res
