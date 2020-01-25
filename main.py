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
paths_dict = {}
temp_dict = {}
temp_list = []

def api_gen (url):
    value = requests.get(url).text
    temp_list = [x for x in value.splitlines()]
    if len(temp_list) <= 1:
        if requests.get(url+temp_list[0]).status_code == 404:
            return { 'value' : temp_list[0] }
        else:
            return { 'key' : temp_list[0] }
    else:
        print('inside api gen temp list is : ', temp_list)
        return { 'keys' : temp_list }

def dict_gen (url):
    api_call = api_gen(url)
    print('value of api call is: ', api_call)
    if 'value' in api_call:
        return api_call["value"]
    elif 'key' in api_call:
        paths_dict.update({ api_call['key'] : api_gen(url+api_call[ 'key' ]) })
    elif 'keys' in api_call:
        print(api_call['keys'])
        for k in api_call['keys']:
            temp_dict.update({ k, api_gen(url+k) })
        return temp_dict 
    return

dict_gen(metadata_server)
print("Dictionary is: \n ", paths_dict)


# print(requests.get(metadata_server+"[]").status_code)

#@app.route("/", methods=["GET"])
#def hello():
#    path(paths_str)
#    return path_dict
#
#
#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8080)
