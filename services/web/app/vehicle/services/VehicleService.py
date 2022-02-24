from app.providers.service.GobService import GobService
from app.vehicle.models.VehicleRepository import VehicleRepository

class VehicleService:

  def __init__(self):
    self.vehicleRepository = VehicleRepository()
    self.gobService = GobService()

  def get_all(self):
    vehicles = self.vehicleRepository.get_all()

    if len(vehicles) == 0:
      vehicles = self.gobService.get_vehicle_and_alcaldias()
    
    return [vehicle.serialize() for vehicle in vehicles or []]

  def get_by_alcaldia_id(self, args):
    alcaldia_id = args.get('alcaldia_id', None)

    vehicles = self.vehicleRepository.get_by_alcaldia_id(alcaldia_id)
    return [vehicle.serialize() for vehicle in vehicles or []]

