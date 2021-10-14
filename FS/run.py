from http import HTTPStatus

import requests
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to the FS server. Use /register followed by your hostname and IP address to register.'


@app.route('/register')
def fs_main():
    ip_address = '192.168.1.208'
    r = requests.post(f'https://{ip_address}:53533', data={'name': request.args.get('hostname'), 'address': ip_address})
    return r.text


@app.route('/fibonacci')
def fibonacci():
    number = request.args.get('number')
    return Response(f"The fibonacci sequence for {number} is: "
                    f"{recursive_fibonacci_helper_function(int(number))}", status=HTTPStatus.OK)


def recursive_fibonacci_helper_function(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        return recursive_fibonacci_helper_function(number - 1) + recursive_fibonacci_helper_function(number - 2)
