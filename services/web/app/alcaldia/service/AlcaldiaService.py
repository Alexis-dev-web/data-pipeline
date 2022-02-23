import os
import requests
import json

from app import app
from app.alcaldia.models.AlcaldiaRepository import AlcaldiaRepository, Alcaldia


class AlcaldiaService:

  def __init__(self):
    self.alcaldiaRepository = AlcaldiaRepository()
    self.URL_GOB = os.environ.get("URL_GOB")

  def get_all(self):
    alcaldias = self.alcaldiaRepository.get_all()

    if len(alcaldias) == 0:
      alcaldias = self.get_alcaldias_from_api_gob()

    return [alcaldia.serialize() for alcaldia in alcaldias or []]

  def get_alcaldias_from_api_gob(self):
    """
      Function to get alcaldias from api https://datos.cdmx.gob.mx/
    """
    url = f'{self.URL_GOB}?resource_id=e4a9b05f-c480-45fb-a62c-6d4e39c5180e'

    try:
      response = requests.get(url)

      data = json.loads(response.content)
      alcaldias = data['result']['records']
      app.logger.error(f'AlcaldiaService#get_alcaldias_from_gob SUCCESS - Retrive alcaldias - alcaldias={len(alcaldias)}')

      return  [self.create_alcaldia_from_api(alcaldia) for alcaldia in alcaldias or []]
    except Exception as error:
      app.logger.error(f'AlcaldiaService#get_alcaldias_from_gob FAILURE - Could not retrive alcaldias - reason={str(error)}')
      return None

  def create_alcaldia_from_api(self, data):
    alcaldia = Alcaldia(data['_id'])
    alcaldia.name = data['nomgeo']
    alcaldia.geo_point = data['geo_point_2d']

    return self.alcaldiaRepository.save(alcaldia)
