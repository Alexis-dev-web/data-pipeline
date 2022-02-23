from app import db

from app.vehicle.models.Vehicle import Vehicle
from services.web.app.BaseModel import Alcaldia


class VehicleRepository:

  def get_by_id(self, id) -> Vehicle:
    return Alcaldia.query.get(id)

  def get_all(self) -> list:
    return Alcaldia.query.all()

  def save(self, vehicle) -> Vehicle:
    db.session.add(vehicle)
    db.session.commit()
    return vehicle

  def update(self, vehicle):
    db.session.commit()
    return vehicle

  def get_by_alcaldia(self, alcaldia_id):
    return Alcaldia.query.filter_by(alcaldia_id=alcaldia_id).first()

