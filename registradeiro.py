# -*- coding: utf-8 -*-
from bottle import route, run, request

db_cache = []


@route('/api/users', method='GET')
def get_users():
    return {'result': db_cache, 'total': len(db_cache)}


@route('/api/users/<user_uid>', method='GET')
def get_user(user_uid):
    for item in db_cache:
        if item['uid'] == user_uid:
            return item
    return {'result': {}}


@route('/api/users', method='POST')
def add_user():
    data = request.json
    db_cache.append(data)

    return data


@route('/api/users/<user_uid>', method='PUT')
def edit_user(user_uid):
    data = request.json
    user = {}

    for item in db_cache:
        if item['uid'] == user_uid:
            user = item
            db_cache.remove(item)

    if user:
        for key, value in data.items():
            user[key] = value
        db_cache.append(user)

    return {'result': user}


@route('/api/users/<user_uid>', method='DELETE')
def delete_user(user_uid):
    for item in db_cache:
        if item['uid'] == user_uid:
            db_cache.remove(item)

    return {'result': db_cache, 'total': len(db_cache)}


run(host='localhost', port=8080,
        debug=True, reloader=True)
