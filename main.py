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
    #print('api_gen url: ', url)
    return parent_key, {parent_key : path_list}, path_list
            


def met_gen(key, path_list, url):
    for p in path_list:
        # path_dict.update({ p : ''})
        print('p', p)
        if p[-1] != '/':
           api_call = api_gen(p, url+p)
           return api_call[1]
        else:
           api_call = api_gen(p, url+p)
           print('api_call[0]: ', api_call[0])
           print('api_call[2]: ', api_call[2])
           print('url: ', url+api_call[0])
           return met_gen(api_call[0], api_call[2], url+api_call[0])
    return

path_list = ["meta-data/"]
path_dict.update(met_gen(None, path_list, metadata_server))
json_data = json.dumps(path_dict, indent=4)


@app.route("/", methods=["GET"])
def hello():
    return render_template('index.html', json_data=json_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
