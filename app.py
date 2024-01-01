from flask import Flask, render_template, request, redirect, url_for
import requests
import os
import json
import pandas as pd
import numpy as np

app = Flask(__name__)
posts = {
    0: {
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}

tickers = {
    0: {
        'symbol': 'MSFT'
    },
    1: {
        'symbol': 'AAPL'
    },
    2: {
        'symbol': 'DXCM'
    }
}


@app.route('/')
def home():
    return render_template('home.jinja2', posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template('404.jinja2', message=f'A post with id {post_id} was not found.')
    return render_template('post.jinja2', post=post)


@app.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id': post_id, 'title': title, 'content': content}

        return redirect(url_for('post', post_id=post_id))
    return render_template('create.jinja2')


@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')


@app.route('/stocks', methods=['GET', 'POST'])
def stocks():
    symbol = request.args.get('symbol')
    ticker_id = len(tickers)
    tickers[ticker_id] = {'id': ticker_id, 'symbol': symbol}
    return render_template('stocks.html', tickers=tickers)



os.chdir("/Users/astralconvict/python-docs-hello-world")

# retrieve from
endpoint = 'https://data.alpaca.markets/v2'
key = json.loads(open("key.txt", 'r').read())

symbol = "msft"
bar_url = endpoint + "/stocks/{}/bars".format(symbol)
params = {"start": "2020-07-20",
            "limit": 600,
            "timeframe": "1Day"
        }

@app.route('/stock-data')
def stock_data():
    data = {"bars": [], "next_page_token": '', "symbol": symbol}
    dataTime = ["test"]
    while True:
        r = requests.get(bar_url, headers=key, params=params)
        r = r.json()
        dataTime += r["bars"][0]["t"]
        if r["next_page_token"] is None:
            data["bars"] += r["bars"]
            break
        else:
            params["page_token"] = r["next_page_token"]
            data["bars"] += r["bars"]
            data["next_page_token"] = r["next_page_token"]
        
    return render_template("dashboard.jinja2", data=data, dataTime=dataTime)





if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)