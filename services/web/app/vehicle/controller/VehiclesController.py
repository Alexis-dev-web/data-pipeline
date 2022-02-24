from flask import request
from flask.json import jsonify
from flask_restful import Resource, abort

from app import app
from app.vehicle.services.VehicleService import VehicleService
from app.vehicle.services.VehicleValidator import VehicleValidator
from app.util.RequestExceptions import ValueRequiredException


class VehiclesController(Resource):

  def __init__(self):
    self.vehicleService = VehicleService()
    self.vehicleValidator = VehicleValidator()

  def get(self):
    app.logger.info(f"VehiclesController#get START - Request recieved - userAgent={request.user_agent.string}")

    try:
      search = request.args.get('search', None)

      if search == 'ALCALDIA':
        self.vehicleValidator.validate_get_all_by_alcaldia_id(request.args)
        response = self.vehicleService.get_by_alcaldia_id(request.args)
      else:
        response = self.vehicleService.get_all()

      app.logger.info(f"VehiclesController#get SUCCESS - Get all vehicles - totalvehicles={len(response)}")

      return jsonify(data=response)
    except ValueRequiredException as vex:
      return abort(400, message=str(vex))
    except AssertionError as assertionError:
      error_message = str(assertionError)
      app.logger.error(f'VehicleController#get FAILURE - Can not get vehicles - reason={error_message}')
      return abort(400, message=error_message)

