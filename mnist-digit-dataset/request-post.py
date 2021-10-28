import cv2
import json
import base64
import argparse
import requests

SERVER_URL = "http://127.0.0.1:8080/"
ROUTE = "inference"

IMG_SHAPE = (1, 28, 28, 1)

API_ENDPOINT = SERVER_URL + ROUTE

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False,
                help="path of the image")
args = vars(ap.parse_args())
try:
    image_path = args['image']

    img = cv2.imread(image_path, 0).reshape(IMG_SHAPE)
    json_data = json.dumps({"instances": img.tolist()})

    results = requests.post(url=API_ENDPOINT, json=json_data)
    print(results.text)
except:
    print('Something went wrong!')