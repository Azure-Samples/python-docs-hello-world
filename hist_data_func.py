# from flask import Blueprint
# import requests
# import os
# import json
# import pandas as pd

# views = Blueprint('views', __name__)


# os.chdir("/Users/astralconvict/python-docs-hello-world")

# # retrieve from
# endpoint = 'https://data.alpaca.markets/v2'
# key = json.loads(open("key.txt", 'r').read())

# symbol = input()
# bar_url = endpoint + "/stocks/{}/bars".format(symbol)
# params = {"start": "2020-06-27",
#             "limit": 600,
#             "timeframe": "1Day"
#         }


# def hist_data(symbols, start="2021-05-05", timeframe="1Hour", limit=600, end=""):
#     df_data_tickers = {}

#     r = requests.get(bar_url, headers=key, params=params)
#     json_dump = r.json()
#     for symbol in json_dump:
#         temp = pd.DataFrame(json_dump[symbols])
#         temp.rename({"t": "time", "o": "open", "h": "high", "l": "low", "c": "close", "v": "volume"}, axis=1,
#                     inplace=True)
#         temp["time"] = pd.to_datetime(temp["time"], unit="s")
#         temp.set_index("time", inplace=True)
#         temp.index = temp.index.tz_localize("UTC").tz_convert("America/Detroit")
#     return temp


# @views.route('/stock-data')
# def stock_data():
#     data = {"bars": [], "next_page_token": '', "symbol": symbol}
#     while True:
#         r = requests.get(bar_url, headers=key, params=params)
#         r = r.json()
#         if r["next_page_token"] is None:
#             data["bars"] += r["bars"]
#             break
#         else:
#             params["page_token"] = r["next_page_token"]
#             data["bars"] += r["bars"]
#             data["next_page_token"] = r["next_page_token"]

#     df_data = pd.DataFrame(data["bars"])
#     df_data.rename({"t": "time", "o": "open", "h": "high", "l": "low", "c": "close", "v": "volume"}, axis=1,
#                 inplace=True)
#     df_data["time"] = pd.to_datetime(df_data["time"])
#     df_data.set_index("time", inplace=True)
#     df_data.index = df_data.index.tz_convert("America/Detroit")
#     print(df_data)


