import requests

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def root():
    return ''

@app.route('/quote')
def quote():
    token = request.args.get('token')
    symbol = request.args.get('symbol')
    payload = {'token' : token, 'symbol': symbol}
    r = requests.get('https://finnhub.io/api/v1/quote', params=payload)
    data = r.json()
    return str(data['c'])
