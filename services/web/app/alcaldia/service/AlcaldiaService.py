from app.alcaldia.models.AlcaldiaRepository import AlcaldiaRepository
from app.providers.service.GobService import GobService


class AlcaldiaService:

  def __init__(self):
    self.alcaldiaRepository = AlcaldiaRepository()
    self.gobService = GobService()

  def get_all(self):
    alcaldias = self.alcaldiaRepository.get_all()

    if len(alcaldias) == 0:
      alcaldias = self.gobService.attach_save_vehicle()

    return [alcaldia.serialize() for alcaldia in alcaldias or []]

