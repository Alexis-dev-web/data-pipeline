import json

from tests.base_core import BaseCore 
from unittest.mock import MagicMock, patch
from app.vehicle.models.VehicleRepository import Vehicle, VehicleRepository


class TestVehicleController(BaseCore):

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

  def test_get_vehicle(self):
    test_vehicle = self.build_test_vehicle(1, 2)

    p = patch('app.vehicle.models.VehicleRepository.VehicleRepository.get_by_vehicle', MagicMock(return_value=test_vehicle))
    p.start()

    response = self.app.get(f"/apiV1/vehicle?vehicle_id={test_vehicle.id}", 
                                headers={"Content-Type": "application/json"})
        
    data = json.loads(response.data.decode('utf-8'))

    self.assertEqual(200, response.status_code)
    self.assertEqual(test_vehicle.id, data['data']['id'])
    p.stop()

  def test_get_vehicle_missing_vehicle_id(self):
    response = self.app.get(f"/apiV1/vehicle?", 
                                headers={"Content-Type": "application/json"})
        
    data = json.loads(response.data.decode('utf-8'))

    self.assertEqual(400, response.status_code)
    self.assertEqual('Vehicle id required', data['message'])
  
  def test_get_vehicle_vehicle_does_not_exist(self):
    p = patch('app.vehicle.models.VehicleRepository.VehicleRepository.get_by_vehicle', MagicMock(return_value=None))
    p.start()

    response = self.app.get(f"/apiV1/vehicle?vehicle_id={9}", 
                                headers={"Content-Type": "application/json"})
        
    data = json.loads(response.data.decode('utf-8'))

    self.assertEqual(400, response.status_code)
    self.assertEqual('Vehicle does not exist', data['message'])
    p.stop()