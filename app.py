import os
from flask import Flask, render_template, request, redirect
import google.cloud.logging
import requests
import logging
import json

URL = os.environ.get("URL", "http://localhost:8082")
DEBUG = os.environ.get("DEBUG", True)
PORT = os.environ.get("PORT", 5000)

# Instantiates a client
client = google.cloud.logging.Client()

# Connects the logger to the root logging handler; by default this captures
# all logs at INFO level and higher
client.setup_logging()

app = Flask(__name__)

@app.route("/")
def home():
  logging.info('home page requested')
  try:
    data = requests.get(URL + '/events').content
    # Parse JSON into a python object with attributes corresponding to dict keys.
    model = json.loads(data)
  except Exception:
    # backend is down, so provide alternative data
    model = {}
  return render_template("home.html", model=model)

@app.route("/event", methods=['POST'])
def create_happening():
  logging.info('event submitted')
  headers = {
      'Content-Type': 'application/json'
  }
  data = request.form.to_dict(flat=True)
  requests.post(URL + '/event', headers=headers, data=json.dumps(data))
  return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
