"""from flask import Flask, redirect, request
import requests
import random
import string

app = Flask(__name__)

client_id = '4e2fc400f8134ab8bfc2419892d7d938'
redirect_uri = 'http://localhost:5000/callback'
client_secret='83e605412e9841a2831ac765eb1d499c'
def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

@app.route('/login')
def login():
    state = generate_random_string(16)
    scope = 'user-read-private user-read-email'

    params = {
        'response_type': 'code',
        'client_id': client_id,
        'client_secret':client_secret,
        'scope': scope,
        'redirect_uri': redirect_uri,
        'state': state
    }

    spotify_authorize_url = 'https://accounts.spotify.com/authorize'
    authorization_url = spotify_authorize_url + '?' + '&'.join([f'{key}={value}' for key, value in params.items()])
    
    return redirect(authorization_url)

if __name__ == '__main__':
    app.run()"""
from dotenv import load_dotenv
import os
import json
import base64
from requests import post, get
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret= os.getenv("CLIENT_SECRET")

print(client_secret)

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64=str(base64.b64encode(auth_bytes), "utf-8")
    url="https://accounts.spotify.com/api/token"
    headers ={ 
        "Authorization": "Basic " + auth_base64,
        "Content-Type":"application/x-www-form-urlencoded"

    }
    data = {"grant_type": "client_credentials"}
    result = post(url,headers=headers, data=data)
    json_results=json.loads(result.content)
   
    return json_results['access_token']
def get_auth_headers(token):
    return {
         "Authorization":'Bearer    ' + token
        }
def get_artist(artist):
    token=get_token()
    url="https://api.spotify.com/v1/search"
    headers =get_auth_headers(token)
    query= f"?q={artist}&type=artist&limit=1"
    query_url=url+query
    result= get(query_url, headers=headers)
    json_result=json.loads(result.content)
    return(json_result)
#https://api.spotify.com/v1/me/player/recently-played

    








