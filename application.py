from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


app = Flask(__name__)

modelfile = 'model.pickle'
model = p.load(open(modelfile, 'rb'))

@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = 'models/final_prediction.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0')


"""
app = Flask(__name__)

modelfile = 'model.pickle'
model = p.load(open(modelfile, 'rb'))

@app.route("/")
def makecalc():
    data = [[1, 1, 70, 1, 1, 100.25]]
    prediction = np.array2string(model.predict(data))
    return prediction

"""