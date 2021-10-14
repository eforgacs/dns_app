from http import HTTPStatus

import requests
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'US is working!'


@app.route('/fibonacci')
def us_main():
    if not [x for x in (request.args.get('hostname'), request.args.get('fs_port'), request.args.get('number'), request.args.get('as_ip'), request.args.get('as_port')) if x is None]:
        return Response("Bad request", status=HTTPStatus.BAD_REQUEST)
    else:
        print(f"Success. Input information is as follows: {request.args.get('hostname')}, {request.args.get('fs_port')}, {request.args.get('number')}, {request.args.get('as_ip')}, {request.args.get('as_port')}")
        ip_info = {'name': request.args.get('hostname'), 'fs_port': request.args.get('fs_port')}
        r = requests.get(f"https://{request.args.get('as_ip')}:{request.args.get('as_port')}", params=ip_info)
        if r.status_code == HTTPStatus.NOT_FOUND:
            return f"Hostname not found. Status:{r.status_code}"
        print(f"https://{r.text}:{request.args.get('fs_port')}/fibonacci?number={request.args.get('number')}")
        r = requests.get(f"https://{r.text}:{request.args.get('fs_port')}/fibonacci?number={request.args.get('number')}")
        return r.text
