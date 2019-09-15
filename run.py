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
import requests
import json
import sys
import numpy
import picamera
from time import sleep

# Import helper functions
#import tutorial_helpers as helpers

# Import the Python wrapper for the ELL model
#import model

#res = requests.get('https://gateway.watsonplatform.net/visual-recognition/api', auth=('apikey', 'iYZxsGs7z0-FxsgZmsaBqhkcf4NdMbM15WmwayaIAOr7'))

sys.path.append('usr/local/lib/python3/site-packages')

def get_img(camera):
    if camera:
        ret, frame = camera.read()
        if not ret:
            raise Exception("Shit didn't work")
        return frame
    return None

def main():
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture('./test-img.jpg')
    camera.stop_preview()

    image = get_img(camera)

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
    print(obj)
    x1 = obj['location']['left']
    y1 = obj['location']['top']
    x2 = x1 + obj['location']['width']
    y2 = y1 + obj['location']['height']

    if threshold > 0.6:
        cleanedList.append([x1,y1,x2,y2])

for box in cleanedList:
    currentImg = cv2.rectangle(currentImg, (box[0],box[1]),(box[2],box[3]),(255,0,0),2)


cv2.imwrite('new.png',currentImg)

if __name__ == "__main__":
    main()
