from flask import Flask
import requests
import os

app = Flask(__name__)

backend_url = os.getenv('BACKEND_URL', 'http://backend:5000/')

@app.route('/')
def home():
    response = requests.get(backend_url)
    return response.json()["message"]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
