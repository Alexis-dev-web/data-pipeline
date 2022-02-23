# from app.providers.service.GobService import GobService
from app.vehicle.models.VehicleRepository import VehicleRepository

class VehicleService:

  def __init__(self):
    self.vehicleRepository = VehicleRepository()
    # self.gobService = GobService()

  def get_all(self):
    vehicles = self.vehicleRepository.get_all()

    # if len(vehicles) == 0:
    #   vehicles = self.gobService.get_vehicles_from_api_gob()
    
    return [vehicle.serialize() for vehicle in vehicles or []]
    