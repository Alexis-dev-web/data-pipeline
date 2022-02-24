import os
import requests
import json
import threading

from app import app
from app import app
from app.alcaldia.models.AlcaldiaRepository import Alcaldia, AlcaldiaRepository
from app.vehicle.models.VehicleRepository import Vehicle, VehicleRepository



class GobService:

  def __init__(self):
    self.alcaldiaRepository = AlcaldiaRepository()
    self.vehicleRepository = VehicleRepository()
    self.URL_GOB = os.environ.get("URL_GOB")
    self.URL_GEO = os.environ.get("URL_GEO")
    self.GEO_KEY = os.environ.get("GEO_KEY")

  def get_alcaldias_from_api_gob(self):
    """
      Function to get alcaldias from api https://datos.cdmx.gob.mx/
    """
    url = f'{self.URL_GOB}?resource_id=e4a9b05f-c480-45fb-a62c-6d4e39c5180e'

    try:
      response = requests.get(url)

      data = json.loads(response.content)
      alcaldias = data['result']['records']
      app.logger.error(f'GobService#get_alcaldias_from_gob SUCCESS - Retrive alcaldias - alcaldias={len(alcaldias)}')

      return  [self.create_alcaldia_from_api(alcaldia) for alcaldia in alcaldias or []]
    except Exception as error:
      app.logger.error(f'GobService#get_alcaldias_from_gob FAILURE - Could not retrive alcaldias - reason={str(error)}')
      return None

  def create_alcaldia_from_api(self, data):
    alcaldia = Alcaldia(data['_id'])
    alcaldia.name = self.get_alcaldia_in_localization(data['geo_point_2d'])
    alcaldia.geo_point = data['geo_point_2d']

    return self.alcaldiaRepository.save(alcaldia)

  def get_vehicles_from_api_gob(self):
    """
      Function to get vehicles from api https://datos.cdmx.gob.mx/
    """
    url = f'{self.URL_GOB}?resource_id=ad360a0e-b42f-482c-af12-1fd72140032e&limit=20'

    try:
      response = requests.get(url)

      data = json.loads(response.content)
      vehicles = data['result']['records']
      app.logger.error(f'GobService#get_vehicles_from_api_gob SUCCESS - Retrive vehicles - vehicles={len(vehicles)}')

      return  [self.create_vehicle_from_api(vehicle) for vehicle in vehicles or []]
    except Exception as error:
      app.logger.error(f'GobService#get_vehicles_from_api_gob FAILURE - Could not retrive vehicles - reason={str(error)}')
      return None

  def create_vehicle_from_api(self, data):
    vehicle = Vehicle(data['_id'])
    vehicle.vehicle_current_status = data['vehicle_current_status']
    vehicle.trip_start_date = data['trip_start_date']
    vehicle.trip_route_id = data['trip_route_id']
    vehicle.trip_schedule_relationship = data['trip_schedule_relationship']
    vehicle.trip_id = data['trip_id']
    vehicle.position_speed = data['position_speed']
    vehicle.vehicle_label = data['vehicle_label']
    vehicle.vehicle_id = data['vehicle_id']
    vehicle.updated_at = data['date_updated']
    
    localization = self.get_alcaldia_in_localization(data['geographic_point'])
    alcaldia = self.alcaldiaRepository.get_by_name(localization)

    vehicle.geographic_point = data['geographic_point']
    vehicle.alcaldia_id = alcaldia.id if alcaldia else None

    return self.vehicleRepository.save(vehicle)

  def attach_save_vehicles_from_background(self):
    """
        When get alcaldias this method get all vehicles in background 
    """
    return self.get_vehicles_from_api_gob()

  def attach_save_vehicle(self):
    alcaldias = self.get_alcaldias_from_api_gob()
    app.logger.info(f"GobService#attach_save_vehicle INFO - Trying to attach vehicles")
    x = threading.Thread(target=self.attach_save_vehicles_from_background())
    x.start()

    return alcaldias

  def get_vehicle_and_alcaldias(self):
    alcaldias = self.get_alcaldias_from_api_gob()

    return self.get_vehicles_from_api_gob()

  def get_alcaldia_in_localization(self, geo_point):
    """
      Get the alcaldia that corresponds to geographic point
    """
    url = f"{self.URL_GEO}/reverse?access_key={self.GEO_KEY}&query={geo_point}&limit=1"

    response = requests.get(url)
    data = json.loads(response.content)

    if len(data['data']) > 0:
      return data['data'][0]['county']
    
    return None