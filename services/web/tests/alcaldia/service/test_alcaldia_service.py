from unittest.mock import MagicMock, patch

from tests.base_core import BaseCore
from app.BaseModel import Alcaldia
from app.alcaldia.service.AlcaldiaService import AlcaldiaService


class TestAlcaldiaService(BaseCore):

  def builld_test_alcaldia(self, id):
    alcaldia = Alcaldia(id)
    alcaldia.name = 'Tlahuac'
    alcaldia.geo_point = '19.2689765031,-99.2684129061'

    return alcaldia

  def test_get_all(self):
    alcaldia = self.builld_test_alcaldia(1)
    alcaldia_2 = self.builld_test_alcaldia(2)

    p = patch('app.providers.service.GobService.GobService.get_alcaldias_from_api_gob', MagicMock(return_value=[alcaldia, alcaldia_2]))
    p1 = patch('app.alcaldia.models.AlcaldiaRepository.AlcaldiaRepository.get_all', MagicMock(return_value=[]))
    p.start()
    p1.start()

    alcaldia_service = AlcaldiaService()
    response = alcaldia_service.get_all()

    self.assertEqual(2, len(response))
    p.stop()
    p1.stop()
  
  def test_get_all_without_call_api(self):
    alcaldia = self.builld_test_alcaldia(1)
    alcaldia_2 = self.builld_test_alcaldia(2)

    p = patch('app.alcaldia.models.AlcaldiaRepository.AlcaldiaRepository.get_all', MagicMock(return_value=[alcaldia, alcaldia_2]))
    p.start()

    alcaldia_service = AlcaldiaService()
    response = alcaldia_service.get_all()

    self.assertEqual(2, len(response))
    p.stop()

