from app.util.RequestExceptions import ValueRequiredException
from app.util.error_mesages import messages

from app.vehicle.models.VehicleRepository import VehicleRepository
from app.alcaldia.models.AlcaldiaRepository import AlcaldiaRepository


class VehicleValidator:

  def __init__(self):
    self.vehicleRepository = VehicleRepository()
    self.alcaldiaRepossitory = AlcaldiaRepository()

  def validate_get_by_vehicle_id(self, vehicle_id):
    if not vehicle_id:
      raise ValueRequiredException(messages['vehicle_id_required'])
    
    vehicle = self.vehicleRepository.get_by_vehicle(vehicle_id)
    if not vehicle:
      raise AssertionError(messages['vehicle_not_exist'])

    return vehicle

  def validate_get_all_by_alcaldia_id(self, args):
    alcaldia_id = args.get('alcaldia_id', None)

    if not alcaldia_id:
      raise ValueRequiredException(messages['alcaldia_id_required'])
    
    alcaldia = self.alcaldiaRepossitory.get_by_id(alcaldia_id)
    if not alcaldia:
      raise AssertionError(messages['alcaldia_not_exist'])

