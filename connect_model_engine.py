#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:52:27 2018

@author: cheeloongng
"""

import requests
import pickle
import pandas as pd

API_HOST = 'http://13.59.233.239:5001'

TEST_API = '/test_endpoint'
PREDICT_API = '/predict'
TRAIN_API = '/train_endpoint'

def test_endpoint():
    print('<client>Test connection')
    r = requests.get(API_HOST + TEST_API)
    
    if r.status_code == 200:
        print('connection successful')
        print("request's text>", r.text)
    else:
        print('Problem',r.status_code)




def main():
    test_endpoint()
    

# Entry point for application (i.e. program starts here)
if __name__ == '__main__':
    main()