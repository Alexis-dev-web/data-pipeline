from app import db

from app.vehicle.models.Vehicle import Vehicle


class VehicleRepository:

  def get_by_id(self, id) -> Vehicle:
    return Vehicle.query.get(id)

  def get_all(self) -> list:
    return Vehicle.query.all()

  def save(self, vehicle) -> Vehicle:
    db.session.add(vehicle)
    db.session.commit()
    return vehicle

  def update(self, vehicle):
    db.session.commit()
    return vehicle

  def get_by_vehicle(self, vehicle_id):
    return Vehicle.query.filter_by(vehicle_id=vehicle_id).first()

  def get_by_alcaldia_id(self, alcaldia_id):
    return Vehicle.query.filter_by(alcaldia_id=alcaldia_id).all()
