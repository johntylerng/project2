#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:23:38 2018

@author: cheeloongng
"""
import sys
import os
import shutil
import traceback
from utils import model_utils
from flask import Flask
from sklearn.externals import joblib

app = Flask(__name__)

model = None

@app.route('/test_endpoint', methods=['GET'])
def test_connection():
    print('somebody is here')
    return 'connected to server'

@app.route('/train_endpoint', methods=['POST'])
def train_model():
    print('training model...wait')
    
    return 'success'

@app.route('/predict',methods=['POST'])
def predict():
    print('predicting....wait')
    return "predicted"

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except Exception as e:
        port = 5001

    try:
        model = joblib.load(model_utils.MODEL_FILE_NAME)
        print('model loaded')
        
    except Exception as e:
        print('No model here')
        print('Train first')
        print(str(e))
        model = None

    app.run(host='0.0.0.0', port=port, debug=True)

        
