import json
import os

from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/home')
def welcome():
    return "This is the AS main page."


@app.route('/', methods=['GET', 'POST'])
def AS():
    file = 'address_map.json'
    if request.method == 'GET':
        key = request.args.get('name')
        if os.path.exists(file):
            with open(file) as json_file:
                file_empty = bool(os.path.getsize(file) == 0)
                if not file_empty:
                    data = json.load(json_file)
                    if key is None or not data.get(key):
                        return Response("Unknown hostname.", status=404)
                    else:
                        address = data.get(key)
                        return Response(address, status=200)
                else:
                    return Response("Empty JSON file.", status=404)
        else:
            with open(file, 'w') as json_file:
                data = json.load(json_file)
                if key is None or not data.get(key):
                    return Response("Unknown hostname.", status=404)
                else:
                    address = data.get(key)
                    return Response(address, status=200)

    else:
        data_get = request.form
        host_name = data_get['name']
        ip_address = data_get['address']
        my_dict = {host_name: ip_address}
        with open(file, 'w') as json_file:
            json.dump(my_dict, json_file)
        return Response("Registered.", status=200)


app.run(host='0.0.0.0',
        port=53533,
        debug=True)
