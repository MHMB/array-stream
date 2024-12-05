from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from .config import Config
from pymongo import MongoClient

socketio = SocketIO()
mongo_client = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Initialize MongoDB
    global mongo_client
    mongo_client = MongoClient(app.config['MONGO_URI'])
    
    # Register blueprints
    from .routes import api
    app.register_blueprint(api, url_prefix='/api')
    
    # Initialize SocketIO
    socketio.init_app(app, cors_allowed_origins="*")
    
    # Import socket events
    from . import socket_events
    
    return app