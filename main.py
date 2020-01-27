from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

# func to recursively return paths
metadata_server = "http://169.254.169.254/latest/"
metadata = {}
path_dict = {}
temp_dict = {}

def api_gen(key, url):
    value = requests.get(url).text
    path_list = [x for x in value.splitlines()]
    parent_key = key
    return parent_key, path_list


def met_gen(path_list, url):
    for p in path_list:
        if p[-1] != '/':
           api_call = api_gen(p, url+p)
           update(path_dict, api_call[0], api_call[1])
        else:
           api_call = api_gen(p, url+p)
           update(path_dict, api_call[0], api_call[1])
           met_gen(api_call[1], url+api_call[0])
    return

def update(dic, key, value):
    for k,v in dic.items():
        if k == key:
            dic[k] = value
        elif isinstance(v, dict):
            update(dic.get(k), key, value)
    return

path_list = ["meta-data/"]
met_gen(path_list, metadata_server)
print(path_dict)
json_data = json.dumps(path_dict, indent=4)


@app.route("/", methods=["GET"])
def hello():
    return render_template('index.html', json_data=json_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
