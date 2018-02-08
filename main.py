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
import pandas as pd
import pickle

app = Flask(__name__)

TRAINING_FILE_PATH = 'data/university_data_2016.csv'
model = None
model_columns = None


@app.route('/test_endpoint', methods=['GET'])
def test_connection():
    print('somebody is here')
    return 'connected to server'

@app.route('/train_endpoint', methods=['POST'])
def train_model():
    print('training model...wait')
    
    return 'success'

@app.route('/train_endpoint_without_file', methods=['GET'])
def train_model_without_file():
    print('training model...wait')
    df = pd.read_csv(TRAINING_FILE_PATH)
    global model_columns, model
    model_columns, model = model_utils.train(df)
    #joblib.dump(model_columns, model_utils.MODEL_COLUMNS_FILE_NAME)
    #joblib.dump(model, model_utils.MODEL_FILE_NAME)
    pickle.dump(model, open(model_utils.MODEL_FILE_NAME, 'wb'))
    
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

        
