from app.alcaldia.controller.AlcaldiasController import AlcaldiasController
from app.vehicle.controller.VehiclesController import VehiclesController
from app.vehicle.controller.VehicleController import VehicleController


def create_routes(api):
  """
    General routes
  """
  api.add_resource(AlcaldiasController, '/apiV1/alcaldias')
  api.add_resource(VehiclesController, '/apiV1/vehicles')
  api.add_resource(VehicleController, '/apiV1/vehicle')
