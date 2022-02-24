from unittest.mock import MagicMock, patch

from tests.base_core import BaseCore
from app.vehicle.models.VehicleRepository import Vehicle, VehicleRepository
from app.vehicle.services.VehicleService import VehicleService


class TestAlcaldiaService(BaseCore):

  def build_test_vehicle(self, alcaldia_id, id):
    vehicle = Vehicle(id)
    vehicle.vehicle_id = 2
    vehicle.vehicle_label = 469
    vehicle.vehicle_current_status = 1
    vehicle.geographic_point = '19.2689765031,-99.2684129061'
    vehicle.position_speed = 208
    vehicle.trip_schedule_relationship = 90
    vehicle.trip_start_date = 154646
    vehicle.trip_route_id = 12
    vehicle.trip_id = 1
    vehicle.alcaldia_id = alcaldia_id

    return vehicle

  def test_get_all(self):
    test_vehicle = self.build_test_vehicle(2, 1)
    test_vehicle_2 = self.build_test_vehicle(1, 9)

    p = patch('app.providers.service.GobService.GobService.get_vehicle_and_alcaldias', MagicMock(return_value=[test_vehicle, test_vehicle_2]))
    p1 = patch('app.vehicle.models.VehicleRepository.VehicleRepository.get_all', MagicMock(return_value=[]))
    p.start()
    p1.start()

    vehicle_service = VehicleService()
    response = vehicle_service.get_all()

    self.assertEqual(2, len(response))
    p.stop()
    p1.stop()
  
  def test_get_all_without_call_api(self):
    test_vehicle = self.build_test_vehicle(2, 1)
    test_vehicle_2 = self.build_test_vehicle(1, 9)

    p = patch('app.vehicle.models.VehicleRepository.VehicleRepository.get_all', MagicMock(return_value=[test_vehicle, test_vehicle_2]))
    p.start()

    vehicle_service = VehicleService()
    response = vehicle_service.get_all()

    self.assertEqual(2, len(response))
    p.stop()
