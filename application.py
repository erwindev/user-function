from app.api.application_api import apiv1
from app import create_app, db
from app.api.utility import api as utility_ns

app = create_app()
app.register_blueprint(apiv1)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,PATCH,POST,DELETE')
    return response

if __name__ == '__main__':
    # Running in Non-Production mode
    import logging

    app.run()
