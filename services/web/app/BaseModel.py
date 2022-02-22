from sqlalchemy import func
from app import db
import uuid


class Alcaldia(db.Model):
  __tablename__ = "Alcaldia"

  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  created_at  = db.Column(db.TIMESTAMP, default=func.current_timestamp())
  updated_at = db.Column(db.TIMESTAMP, default=func.current_timestamp(), onupdate=func.current_timestamp())

  def __init__(self, id):
      self.id = id
  
  def serialize(self):
      return {
          'id': self.id, 
          'name': self.name,
          'created_at': str(self.created_at),
          'updated_at': str(self.updated_at)
      }
