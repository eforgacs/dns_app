from http import HTTPStatus
import json
import os

from flask import Flask, request, Response

app = Flask(__name__)

home = '/home'


@app.route(home)
def welcome():
    return home


@app.route('/', methods=['GET', 'POST'])
def as_main():
    file = 'address_map.json'
    if request.method == 'GET':
        key = request.args.get('name')
        if os.path.exists(file):
            with open(file) as json_file:
                file_empty = bool(os.path.getsize(file) == 0)
                if not file_empty:
                    data = json.load(json_file)
                    if key is None or not data.get(key):
                        return Response("Unknown hostname.", status=HTTPStatus.NOT_FOUND)
                    else:
                        address = data.get(key)
                        return Response(address, status=HTTPStatus.OK)
                else:
                    return Response("Empty JSON file.", status=HTTPStatus.NOT_FOUND)
        else:
            with open(file, 'w') as json_file:
                data = json.load(json_file)
                if key is None or not data.get(key):
                    return Response("Unknown hostname.", status=HTTPStatus.NOT_FOUND)
                else:
                    address = data.get(key)
                    return Response(address, status=HTTPStatus.OK)

    else:
        data_get = request.form
        host_name = data_get['name']
        ip_address = data_get['address']
        my_dict = {host_name: ip_address}
        with open(file, 'w') as json_file:
            json.dump(my_dict, json_file)
        return Response("Registered.", status=HTTPStatus.OK)
