from tests.BaseCase import BaseCase
from app.alcaldia.models.AlcaldiaRepository import Alcaldia, AlcaldiaRepository


class TestAlcaldiaRepository(BaseCase):

  def builld_test_alcaldia(self, id):
    alcaldia = Alcaldia(id)
    alcaldia.name = 'Tlahuac'
    alcaldia.geo_point = '19.2689765031,-99.2684129061'

    return alcaldia

  def test_save_alcaldia(self):
    alcaldia = self.builld_test_alcaldia(1)

    alcaldia_repository = AlcaldiaRepository()
    
    self.assertIsNotNone(alcaldia_repository.save(alcaldia))
  
  def test_update_alcaldia(self):
    alcaldia = self.builld_test_alcaldia(1)

    alcaldia_repository = AlcaldiaRepository()
    alcaldia_repository.save(alcaldia)

    alcaldia.name = 'Iztapalapa'
    response = alcaldia_repository.update(alcaldia)
    
    self.assertEqual('Iztapalapa', response.name)

  def test_get_by_id(self):
    alcaldia = self.builld_test_alcaldia(1)
    test_alcaldia_2 = self.builld_test_alcaldia(2)
    test_alcaldia_2.name = 'Iztapalapa'

    alcaldia_repository = AlcaldiaRepository()
    alcaldia_repository.save(alcaldia)
    alcaldia_repository.save(test_alcaldia_2)

    response = alcaldia_repository.get_by_id(alcaldia.id)
    
    self.assertEqual(alcaldia, response)
  
  def test_get_all(self):
    alcaldia = self.builld_test_alcaldia(1)
    test_alcaldia_2 = self.builld_test_alcaldia(2)
    test_alcaldia_2.name = 'Iztapalapa'

    alcaldia_repository = AlcaldiaRepository()
    alcaldia_repository.save(alcaldia)
    alcaldia_repository.save(test_alcaldia_2)

    response = alcaldia_repository.get_all()
    
    self.assertEqual(2, len(response))
