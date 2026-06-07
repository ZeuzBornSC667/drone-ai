
from flask import Flask
from flask_socketio import SocketIO

def create_dashboard(state, pipeline):
    app = Flask(__name__)
    socketio = SocketIO(app)

    @app.route('/')
    def index():
        return "Drone AI Running"

    return app, socketio
