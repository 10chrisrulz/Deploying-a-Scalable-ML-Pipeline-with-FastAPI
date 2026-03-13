import json

import requests

BASE_URL = "http://127.0.0.1:8000"

# TODO: send a GET using the URL http://127.0.0.1:8000
r = requests.get(BASE_URL)

# TODO: print the status code and welcome message
print(f"Status Code: {r.status_code}")
print(f"Result: {r.json().get('message', r.text)}")

data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# TODO: send a POST using the data above (inference endpoint)
r = requests.post(f"{BASE_URL}/data/", json=data)

# TODO: print the status code and result
print(f"Status Code: {r.status_code}")
print(f"Result: {r.json().get('result', r.text)}")
