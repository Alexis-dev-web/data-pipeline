from unittest.mock import MagicMock, patch

from tests.base_core import BaseCore
from app.BaseModel import Alcaldia
from app.providers.service.GobService import GobService


class TestGobService(BaseCore):

  def builld_test_alcaldia(self, id):
    alcaldia = Alcaldia(id)
    alcaldia.name = 'Tlahuac'
    alcaldia.geo_point = '19.2689765031,-99.2684129061'

    return alcaldia

  def test_craete_alcaldia_from_api(self):
    alcaldia = self.builld_test_alcaldia(1)

    data = {
      '_id': 2,
      'nomgeo': alcaldia.name,
      'geo_point_2d': alcaldia.geo_point
    }

    p = patch('app.alcaldia.models.AlcaldiaRepository.AlcaldiaRepository.save', MagicMock(return_value=alcaldia))
    p1 = patch('app.providers.service.GobService.GobService.get_alcaldia_in_localization', MagicMock(return_value='Iztapalapa'))
    p.start()
    p1.start()

    gob_service = GobService()
    
    response = gob_service.create_alcaldia_from_api(data)

    self.assertEqual(alcaldia, response)
    p.stop()
    p1.stop()