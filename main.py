from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

metadata_server = "http://metadata/computeMetadata/v1/instance/"
metadata_flavor = {'Metadata-Flavor' : 'Google'}
# gce_id = requests.get(metadata_server + 'id', headers = metadata_flavor).text
# gce_name = requests.get(metadata_server + 'hostname', headers = metadata_flavor).text
# gce_machine_type = requests.get(metadata_server + 'machine-type', headers = metadata_flavor).text
# gce_nics = requests.get(metadata_server + 'network-interfaces/', headers = metadata_flavor).text
# gce_zone = requests.get(metadata_server + 'zone', headers = metadata_flavor).text
gce_all = requests.get(metadata_server + '?recursive=true', headers = metadata_flavor).text
gce_parsed = json.dumps(json.loads(gce_all), indent=4, sort_keys=True)



@app.route("/", methods=["GET"])
def hello():
    return render_template('index.html', gce_parsed=gce_parsed)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
