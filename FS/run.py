import requests
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to the FS server. Use /register followed by your hostname and IP address to register.'


@app.route('/register')
def register():
    host_name = request.args.get('hostname')
    ip_address = '192.168.1.208'
    r = requests.post('https://192.168.1.208:53533', data={'name': host_name, 'address': ip_address})
    return r.text


@app.route('/fibonacci')
def fibonacci():
    number = request.args.get('number')
    return Response(f"The fibonacci sequence for {number} is: "
                    f"{recursive_fibonacci_helper_function(int(number))}", status=200)


def recursive_fibonacci_helper_function(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        return recursive_fibonacci_helper_function(number - 1) + recursive_fibonacci_helper_function(number - 2)


app.run(host='0.0.0.0',
        port=9090,
        debug=True)
