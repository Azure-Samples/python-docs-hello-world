from flask import Flask, request, redirect, url_for, flash, jsonify,render_template
#import numpy as np
import pickle as p
import json

app = Flask(__name__)

@app.route("/")
def makecalc():
    data = [[1, 1, 70, 1, 1, 100.25]]
    qwe=2+2
    listToStr = np.array2string(np.sum(np.array(data)))
    #listToStr="hello"
    return listToStr
    

    #return np.array2string(np.sum(np.array(data)))
    #data = request.get_json()
    #prediction = np.array2string(model.predict(data))

"""
from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


app = Flask(__name__)


#@app.route('/api/', methods=['POST'])
@app.route("/")
def makecalc():
    data = [[1, 1, 70, 1, 1, 100.25]]
    #data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = 'model.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run()
    """