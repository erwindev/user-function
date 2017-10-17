import os
from app.api.application_api import api
from flask import jsonify
from flask_restplus import Resource

SERVICE_NAME = os.environ.get('SERVICE_NAME') or 'not set'
CURRENT_VERSION = os.environ.get('CURRENT_VERSION') or 'not set'


@api.route("/health")
class Health(Resource):
    def get(self):
        """Provides status of 'UP' """
        return jsonify(status='UP')


@api.route("/info")
class Info(Resource):
    def get(self):
        """ Provides name and current version """
        return jsonify(name=SERVICE_NAME, version=CURRENT_VERSION)


@api.route("/api/apptracker/v1/whoami")
class WhoAmi(Resource):
    def get(self):
        """Run the whoami request"""
        return jsonify(whoami="College App User API")
