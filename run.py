#!/usr/bin/env python3
###############################################################################
#
#  Project:  Embedded Learning Library (ELL)
#  File:     tutorial.py
#  Authors:  Byron Changuion
#
#  Requires: Python 3.x
#
###############################################################################

import time
import cv2
import requests
import json


# Import helper functions
#import tutorial_helpers as helpers

# Import the Python wrapper for the ELL model
#import model



#res = requests.get('https://gateway.watsonplatform.net/visual-recognition/api', auth=('apikey', 'iYZxsGs7z0-FxsgZmsaBqhkcf4NdMbM15WmwayaIAOr7'))


params = (
    ('version', '2019-02-11'),
)

files = {
    'features': (None, 'objects'),
    'collection_ids': (None, 'bed5f8bc-ecb9-4397-a256-278f52812823'),
    'images_file': ('dice.png', open('test.jpg', 'rb')),
}

response = requests.post('https://gateway.watsonplatform.net/visual-recognition/api/v4/analyze', params=params, files=files, auth=('apikey', 'iYZxsGs7z0-FxsgZmsaBqhkcf4NdMbM15WmwayaIAOr7'))

output = response.json()
objectsList = output['images'][0]['objects']['collections'][0]['objects']

cleanedList = []
for obj in objectsList:
    threshold = obj['score']
    x1 = obj['left']
    y1 = obj['top']
    x2 = x1 + obj['width']
    y2 = y1 + obj['height']







