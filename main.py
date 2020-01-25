from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

metadata_server = "http://169.254.169.254/latest/meta-data/"
metadata_paths = requests.get(metadata_server).text



@app.route("/", methods=["GET"])
def hello():
    return metadata_paths


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
