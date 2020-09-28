#%%
from flask import Flask, json, send_from_directory
from flask_restful import Api, Resource, reqparse
import requests
import os

app = Flask(__name__)
api = Api(app)

def getUrl(url):
  proxy = { "http"  : "http://127.0.0.1:9001", "https" : "http://127.0.0.1:9001"}
  r = requests.get(url, allow_redirects=True, verify=True, proxies=proxy)
  return r.content

class Update(Resource):
  def get(self, filename):
    version='2.19.4'
    parser = reqparse.RequestParser()
    parser.add_argument('version', type=str)
    if(parser.parse_args()['version']!=None):
      version = parser.parse_args()['version']
    dir_base = os.path.realpath(os.path.dirname(__file__))
    dir_path = "{}/plugins/{}".format(dir_base, version)
    return send_from_directory(dir_path, filename)


class Plugin(Resource):
  def get(self,core,name,version,name_ext):
    url = ' https://archives.jenkins.io/plugins/{}/{}/{}'.format(name,version,name_ext)
    r = None
    dir_base = os.path.realpath(os.path.dirname(__file__))
    dir_path = "{}/plugins/{}".format(dir_base, core)
    file_path =  "{}/{}".format(dir_path, name_ext)
    if(not os.path.exists(file_path)):
      print('{:100} downloading...'.format(url))
      open(file_path, 'wb').write(getUrl(url))
    print('{:100} downloaded...'.format(file_path))
    return send_from_directory(dir_path, name_ext)

#http://127.0.0.1:5000/jenkins/plugins/2.19.4/workflow-cps/2.41/workflow-cps.hpi
#http://127.0.0.1:5000/jenkins/plugins/2.19.4/scriptler/2.9/scriptler.hpi

api.add_resource(Plugin,"/jenkins/plugins/<core>/<name>/<version>/<name_ext>")

#http://127.0.0.1:5000/jenkins/update-center.json?version=2.19.4
api.add_resource(Update,"/jenkins/<path:filename>")

# api.run(debug=True, port=8000)
app.run(debug=True)