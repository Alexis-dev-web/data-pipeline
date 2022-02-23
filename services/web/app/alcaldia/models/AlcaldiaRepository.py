from app import db

from app.BaseModel import Alcaldia


class AlcaldiaRepository:

  def get_by_id(self, id) -> Alcaldia:
    return Alcaldia.query.get(id)

  def get_all(self) -> list:
    return Alcaldia.query.all()

  def save(self, alcaldia) -> Alcaldia:
    db.session.add(alcaldia)
    db.session.commit()
    return alcaldia

  def update(self, alcaldia) -> Alcaldia:
    db.session.commit()
    return alcaldia
