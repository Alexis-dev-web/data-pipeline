from http.client import IM_USED
from flask import request
from flask.json import jsonify
from flask_restful import Resource, abort

from app import app
from app.vehicle.services.VehicleService import VehicleService
from app.vehicle.services.VehicleValidator import VehicleValidator
from app.util.RequestExceptions import ValueRequiredException


class VehicleController(Resource):

  def __init__(self):
    self.vehicleService = VehicleService()
    self.vehicleValidator = VehicleValidator()

  def get(self):
    vehicle_id = request.args.get('vehicle_id', None)
    app.logger.info(f"VehicleController#get START - Request recieved - userAgent={request.user_agent.string}")

    try:
      vehicle = self.vehicleValidator.validate_get_by_vehicle_id(vehicle_id)

      app.logger.info(f"VehicleController#get SUCCESS - Get vehicle by id - vehicleId={vehicle.id}")

      return jsonify(data=vehicle.serialize())
    except ValueRequiredException as vex:
      return abort(400, message=str(vex))
    except AssertionError as assertionError:
      error_message = str(assertionError)
      app.logger.error(f'VehicleController#get FAILURE - Can not get vehicle - reason={error_message}')
      return abort(400, message=error_message)

