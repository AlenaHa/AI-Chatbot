from flask import Flask, Blueprint
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_socketio import SocketIO

from . import config, settings
from .settings import HOST, PORT, PROJECT


# Entire Flask application and its configuration.
app = Flask(__name__)
app.config.from_object(config.config[settings.CONFIG])

# Exposing API capabilities and (de)serialization schemas.
api_bp = Blueprint("api", __name__)
api = Api(api_bp)
ma = Marshmallow(app)

# Websockets.
sio = SocketIO(app)


from . import views


api.errors = views.api.ERRORS
app.register_blueprint(api_bp, url_prefix=views.api.URL_PREFIX)


def run_server(conf=settings.CONFIG):
    app.config.from_object(config.config[conf])
    sio.run(
        app,
        host=HOST,
        port=PORT,
    )
