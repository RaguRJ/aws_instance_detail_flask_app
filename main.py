from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

# getting the key and folder structure / converting text data to string to make further requests
metadata_server = "http://169.254.169.254/latest/meta-data/events/"
#paths = requests.get(metadata_server).text
#paths_list = [x for x in paths.splitlines()]
#print(paths_list)

# func to recursively return paths
metadata_server = "http://169.254.169.254/latest/meta-data/"
metadata = {}
path_dict = {}


def api_gen(key, url):
    value = requests.get(url).text
    path_list = [x for x in value.splitlines()]
    parent_key = key
    return parent_key, path_list
            


def met_gen(key, path_list, url):
    #print(path_list)
    for p in path_list:
        if p[-1] != '/':
            api_call = api_gen(p, url+p)
     #       print(api_call[1])
            path_dict.update({ api_call[0] : api_call[1] })
        else:
            api_call = api_gen(p, url+p)
            if api_call[0] in path_dict:
                print(api_call[0])
                path_dict[api_call[0]] = api_call[1]
            else:
                path_dict.update({ api_call[0] : api_gen(api_call[0], url+p+api_call[1][0]) })
    return

path_list = [x for x in requests.get(metadata_server).text.splitlines()]
met_gen(None, path_list, metadata_server)
json_data = json.dumps(path_dict, indent=4, sort_keys=True)


@app.route("/", methods=["GET"])
def hello():
    return render_template('index.html', json_data=json_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
