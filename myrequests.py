import json
from flask import Flask, request
from flask_cors import CORS
from flask import redirect, url_for

from base import *

app = Flask(__name__)
CORS(app)

HostName = 'localhost:5000/'

def start():
    app.run(host='localhost', debug=True, port=5000)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response

@app.route('/', methods=['GET'])
def good():
    return "good"

@app.route('/<path:short_link>', methods=['GET'])
def def1(short_link):
    if request.method == 'GET':
       if len(short_link) == 6:
            initial_url = find_url(short_link, "short")
            print('/'+ initial_url)
    if (initial_url.startswith('http:\\')) or (initial_url.startswith('https:\\')):
       return redirect(initial_url)
    else:  return redirect('//' + initial_url)


@app.route("/get_short_url", methods=['POST'])
def get_short_url():
    if request.method == 'POST':
        json_data = request.data            # json data from request
        string_data = json.loads(json_data) # dict data from request
        initial_url = string_data['initial_url']    # string big_url
        new_url = gen_unique_url()          # generic new short unique url
        add_url(initial_url, new_url)           # add pair (big_url, new_short_url) to base
    return SiteName + new_url

@app.route("/clear", methods=['GET'])
def clear():
    print('clear_start')
    clear_base()
    return ''
