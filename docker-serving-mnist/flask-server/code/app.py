import os
import json
import requests
import numpy as np
from flask import Flask, request

app = Flask(__name__)
 
@app.route('/')
def health_check():
    return '.: Server is up :.'

@app.route('/inference', methods=['POST'])
def predict():
    json_data = json.dumps(json.loads(request.json))
    headers = {"content-type": "application/json"}
    
    json_response = requests.post('http://tfmodel:8501/v1/models/mnist_digit:predict', data=json_data, headers=headers)
    json_response = json.loads(json_response.content.decode('utf-8'))

    prediction = int(np.array(json_response["predictions"][0]).argmax())
    return json.dumps({'prediction': prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)