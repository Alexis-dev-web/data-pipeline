from sqlalchemy import func
from app import db


class Vehicle(db.Model):
  __tablename__ = "Vehicle"

  id = db.Column(db.Integer(), primary_key=True)
  vehicle_id = db.Column(db.Integer(), nullable=False)
  vehicle_label = db.Column(db.String(255), nullable=True)
  vehicle_current_status = db.Column(db.Integer(), nullable=False)
  geographic_point = db.Column(db.String(50), nullable=False)
  position_speed = db.Column(db.String(50), nullable=False)
  position_odometer = db.Column(db.String(50), nullable=False)
  trip_schedule_relationship = db.Column(db.String(50), nullable=False)
  trip_start_date = db.Column(db.String(50), nullable=False)
  trip_route_id = db.Column(db.Integer())
  trip_id = db.Column(db.Integer(), db.ForeignKey('Alcaldia.id'), nullable=False)
  alcaldia_id = db.Column(db.Integer())
  created_at  = db.Column(db.TIMESTAMP, default=func.current_timestamp())
  updated_at = db.Column(db.TIMESTAMP, default=func.current_timestamp(), onupdate=func.current_timestamp())

  def __init__(self, id=0):
      self.id = id
  
  def serialize(self):
      return {
          'id': self.id, 
          'created_at': str(self.created_at),
          'updated_at': str(self.updated_at)
      }
