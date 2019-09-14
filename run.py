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
from ibm_watson import VisualRecognitionV3

# Import helper functions
#import tutorial_helpers as helpers

# Import the Python wrapper for the ELL model
#import model

visual_recognition = VisualRecognitionV3(
    '2019-02-11',
    iam_apikey='dMbAv-vbgW7a6v8CyEGxtO3YUuajWcdh_QpevaHv5w6x')

with open('./test.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
        owners=["me"]).get_result()
    print(json.dumps(classes, indent=2))


