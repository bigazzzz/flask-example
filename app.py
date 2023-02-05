from kubernetes import config, client
from flask import Flask, make_response
from flask_restful import Api, Resource, reqparse

import json
import os


class Stand(Resource):
    def get(self):
        if os.getenv('STAND') is None:
            return "Not defined", 404
        else:
            return {'stand': os.getenv('STAND')}, 200

class Pods(Resource):
    def get(self, podname):
        return "ok", 200

app = Flask(__name__)
api = Api(app)

@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp

api.add_resource(Stand, "/stand")
if __name__ == '__main__':
    app.run(debug=True)
