import requests
import os

from dotenv import load_dotenv
load_dotenv()

def query(payload, url, headers):
    response = requests.post(url, headers=headers, json=payload)
    return response.json()