from urllib import response
from tests.BaseCase import BaseCase
from app.alcaldia.models.AlcaldiaRepository import Alcaldia, AlcaldiaRepository
from app.vehicle.models.VehicleRepository import Vehicle, VehicleRepository


class TestVehicleRepository(BaseCase):

  def builld_test_alcaldia(self, id):
    alcaldia = Alcaldia(id)
    alcaldia.name = 'Tlahuac'
    alcaldia.geo_point = '19.2689765031,-99.2684129061'

    return alcaldia

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

  def test_save_vehicle(self):
    alcaldia = self.builld_test_alcaldia(1)
    vehicle = self.build_test_vehicle(alcaldia.id, 9)

    alcaldia_repository = AlcaldiaRepository()
    alcaldia_repository.save(alcaldia)

    vehicle_repository = VehicleRepository()
    self.assertIsNotNone(vehicle_repository.save(vehicle))
  
  def test_update_vehicle(self):
    alcaldia = self.builld_test_alcaldia(1)
    vehicle = self.build_test_vehicle(alcaldia.id, 9)

    alcaldia_repository = AlcaldiaRepository()
    alcaldia_repository.save(alcaldia)

    vehicle_repository = VehicleRepository()
    vehicle.position_speed = 90
    response = vehicle_repository.update(vehicle)
    
    self.assertEqual(90, response.position_speed)

  def test_get_by_id(self):
    alcaldia = self.builld_test_alcaldia(1)
    vehicle = self.build_test_vehicle(alcaldia.id, 9)

    alcaldia_repository = AlcaldiaRepository()
    alcaldia_repository.save(alcaldia)

    vehicle_repository = VehicleRepository()
    vehicle_repository.save(vehicle)

    response = vehicle_repository.get_by_id(vehicle.id)
    
    self.assertEqual(vehicle, response)
  
  def test_get_all(self):
    alcaldia = self.builld_test_alcaldia(1)
    vehicle = self.build_test_vehicle(alcaldia.id, 9)
    vehicle_2 = self.build_test_vehicle(alcaldia.id, 10)

    alcaldia_repository = AlcaldiaRepository()
    alcaldia_repository.save(alcaldia)

    vehicle_repository = VehicleRepository()
    vehicle_repository.save(vehicle)
    vehicle_repository.save(vehicle_2)
  
    response = vehicle_repository.get_all()
    
    self.assertEqual(2, len(response))

  def test_get_by_vehicle_id(self):
    alcaldia = self.builld_test_alcaldia(1)
    vehicle = self.build_test_vehicle(alcaldia.id, 9)
    vehicle_2 = self.build_test_vehicle(alcaldia.id, 10)

    alcaldia_repository = AlcaldiaRepository()
    alcaldia_repository.save(alcaldia)

    vehicle_repository = VehicleRepository()
    vehicle_repository.save(vehicle)
    vehicle_repository.save(vehicle_2)
  
    response = vehicle_repository.get_by_vehicle(vehicle.vehicle_id)
    
    self.assertEqual(vehicle, response)

  def test_get_by_alcaldia_id(self):
    alcaldia = self.builld_test_alcaldia(1)
    vehicle = self.build_test_vehicle(alcaldia.id, 9)
    vehicle_2 = self.build_test_vehicle(alcaldia.id, 10)

    alcaldia_repository = AlcaldiaRepository()
    alcaldia_repository.save(alcaldia)

    vehicle_repository = VehicleRepository()
    vehicle_repository.save(vehicle)
    vehicle_repository.save(vehicle_2)
  
    response = vehicle_repository.get_by_alcaldia_id(alcaldia.id)
    
    self.assertEqual(2, len(response))
