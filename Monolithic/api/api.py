import os
import time

from flask import Flask, render_template, request, redirect, url_for, jsonify, g
from service.service import get_content_service, get_user_service, get_provider_service
from service.service import create_content_service, create_provider_service, create_user_service
from service.service import get_user_content_service, user_subscribe_service
import json
from api import app

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', '50.txt'))


@app.before_request
def before_request():
    g.start = time.time()


@app.after_request
def after_request(response):
    diff = time.time() - g.start
    file = open(file_path, 'a+')  # Open a file in append mode
    print('a')
    file.write("," + str(diff))  # Write some text
    file.close()
    print(diff)
    return response


@app.route('/login', methods=['GET'])
def login():
    user_name = request.args.get('user_name')
    user_pass = request.args.get('user_pass')
    res = get_user_service(user_name, user_pass)
    return jsonify(res)


@app.route('/signup', methods=['GET'])
def signup():
    user_name = request.args.get('user_name')
    user_pass = request.args.get('user_pass')
    user_email = request.args.get('user_email')
    res = create_user_service(user_name, user_pass, user_email)
    return jsonify(res)


@app.route('/add-providers', methods=['GET'])
def add_providers():
    provider_name = request.args.get('provider_name')
    srate = request.args.get('srate')
    res = create_provider_service(provider_name, srate)
    return jsonify(res)


@app.route('/add-contents', methods=['GET'])
def add_contents():
    id = request.args.get('content_id')
    name = request.args.get('content_name')
    des = request.args.get('content_des')
    srate = request.args.get('srate')
    provider = request.args.get('provider')
    res = create_content_service(id, name, des, srate, provider)
    return jsonify(res)


@app.route('/get-all-providers', methods=['GET'])
def get_all_providers():
    res = get_provider_service()
    return jsonify(res)


@app.route('/get-all-contents', methods=['GET'])
def get_all_contents():
    res = get_content_service()
    return jsonify(res)


@app.route('/get-user-contents', methods=['GET'])
def get_user_contents():
    user_email = request.args.get("user_email")
    res = get_user_content_service(user_email)
    return jsonify(res)


@app.route('/subscribe-contents', methods=['GET'])
def subscribe_contents():
    email = request.args.get('user_email')
    id = request.args.get('content_id')
    res = user_subscribe_service(email, id)
    return jsonify(res)
