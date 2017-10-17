import os
from flask_restplus import Api
from flask import Blueprint

apiv1 = Blueprint('application_api', __name__, url_prefix='')

service_name = os.getenv('SERVICE_NAME') or 'not set'
version = os.getenv('CURRENT_VERSION') or 'not set'

api = Api(apiv1, version=version, title='{} API'.format(service_name),
          description='Application End Points',
          default=service_name,
          default_label="{} v{}".format(service_name, version))

utility_ns = api.namespace('utility', 'Utility methods')
