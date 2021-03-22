from re import S
from flask import Flask, json, jsonify, request, abort
from flaskr.models import setup_db, Plant
from flask_cors import CORS
import os

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__, instance_relative_config=True)
  setup_db(app)
  CORS(app)

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authontication')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
    return response

  @app.route("/plants", methods=['GET'])
  def get_plants():
  
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    end = start + 10
  
    plants = Plant.query.all()
    formatted_plants = [plant.format() for plant in plants]
  
    return jsonify({
        "success":True,
        "plants": formatted_plants[start:end],
        "total_plants": len(formatted_plants)
      })

  @app.route("/plants/<int:plant_id>")
  def get_specific_plant(plant_id):
    plant = Plant.query.filter(Plant.id == plant_id).one_or_none()

    if plant is None:
      abort(404)
    else:
      return jsonify({
        'success': True,
        'plant': plant.format()
      })

  return app

  ###################
  # Depricated Code #
  ###################

  # Lines: 10 - 17
  # app.config.from_mapping(
  #   SECRET_KEY='dev',
  #   DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
  # )
    
  # if test_config is None:
  #   # load the instance config, if it exists, when not testing 
  #   app.config.from_pyfile('config.py', silent=True)