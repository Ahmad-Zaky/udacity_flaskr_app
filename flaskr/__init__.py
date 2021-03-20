from flask import Flask, json, jsonify
from flask_cors import CORS
import os

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__, instance_relative_config=True)
  cors = CORS(app)
  app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
  )

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authontication')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
    return response
    
  if test_config is None:
    # load the instance config, if it exists, when not testing 
    app.config.from_pyfile('config.py', silent=True)

  @app.route("/")
  def hello():
    return jsonify({"message": "HELLO WORLD!"})
  
  return app