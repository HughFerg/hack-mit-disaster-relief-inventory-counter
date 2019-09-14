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

# Import helper functions
import tutorial_helpers as helpers

# Import the Python wrapper for the ELL model
import model


def get_image_from_camera(camera):
    """Read an image from the camera"""
    if camera:
        ret, frame = camera.read()
        if not ret:
            raise Exception("your capture device is not returning images")
        return frame
    return None


def main():
    # Open the video camera. To use a different camera, change the camera
    # index.
    camera = cv2.VideoCapture(0)

    # Read the category names
    with open("categories.txt", "r") as categories_file:
        categories = categories_file.read().splitlines()

    while (cv2.waitKey(1) & 0xFF) == 0xFF:
        # Get an image from the camera.
        image = get_image_from_camera(camera)

        # Prepare an image for processing
        # - Resize and center-crop to the required width and height while
        #   preserving aspect ratio.
        # - OpenCV gives the image in BGR order. If needed, re-order the
        #   channels to RGB.
        # - Convert the OpenCV result to a std::vector<float>
        input_data = helpers.prepare_image_for_model(
            image, input_shape.columns, input_shape.rows, preprocessing_metadata=preprocessing_metadata)

        # Wrap the resulting numpy array in a FloatVector
        input_data = model.FloatVector(input_data)

        # Send the image to the compiled model and get the predictions vector
        # with scores, measure how long it takes
        start = time.time()
        predictions = model_wrapper.Predict(input_data)
        end = time.time()

        # Get the value of the top 5 predictions
        top_5 = helpers.get_top_n(predictions, 5)

        # Display the image
        cv2.imshow("ELL model", image)

    print("Mean prediction time: {:.0f}ms/frame".format(
        mean_time_to_predict * 1000))

if __name__ == "__main__":
    main()
