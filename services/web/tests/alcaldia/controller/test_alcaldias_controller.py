from app.BaseModel import Alcaldia

import json

from tests.base_core import BaseCore 
from unittest.mock import MagicMock, patch


class TestAlcaldiaController(BaseCore):

  def builld_test_alcaldia(self, id):
    alcaldia = Alcaldia(id)
    alcaldia.name = 'Tlahuac'
    alcaldia.geo_point = '19.2689765031,-99.2684129061'

    return alcaldia

  def test_get_all_alaldias(self):
    test_alcaldia = self.builld_test_alcaldia(3)

    p = patch('app.providers.service.GobService.GobService.get_alcaldias_from_api_gob', MagicMock(return_value=[test_alcaldia]))
    p1 = patch('app.alcaldia.models.AlcaldiaRepository.AlcaldiaRepository.get_all', MagicMock(return_value=[]))
    p.start()
    p1.start()

    response = self.app.get(f"/apiV1/alcaldias", 
                                headers={"Content-Type": "application/json"})
        
    data = json.loads(response.data.decode('utf-8'))

    self.assertEqual(200, response.status_code)
    self.assertEqual(1, len(data['data']))
    p.stop()
    p1.stop()

  def test_get_all_without_call_to_api(self):
    test_alcaldia = self.builld_test_alcaldia(3)

    p = patch('app.alcaldia.models.AlcaldiaRepository.AlcaldiaRepository.get_all', MagicMock(return_value=[test_alcaldia]))
    p.start()

    response = self.app.get(f"/apiV1/alcaldias", 
                                headers={"Content-Type": "application/json"})
        
    data = json.loads(response.data.decode('utf-8'))

    self.assertEqual(200, response.status_code)
    self.assertEqual(1, len(data['data']))
    p.stop()
