import requests
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'US is working!'


@app.route('/fibonacci')
def US():
    host_name = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    x = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')
    if not [x for x in (host_name, fs_port, x, as_ip, as_port) if x is None]:
        return Response("Bad request", status=400)
    else:
        print(f'Success. Input information is as follows: {host_name}, {fs_port}, {x}, {as_ip}, {as_port}')
        ip_info = {'name': host_name, 'fs_port': fs_port}
        r = requests.get(f'https://{as_ip}:{as_port}', params=ip_info)
        if r.status_code == 404:
            return "hostname not found, Status:404"
        ip_address_fs = f'https://{r.text}:{fs_port}/fibonacci?number={x}'
        print(ip_address_fs)
        r = requests.get(ip_address_fs)
        return r.text


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
