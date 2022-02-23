from sqlalchemy import func
from app import db


class Vehicle(db.Model):
  __tablename__ = "Vehicle"

  id = db.Column(db.Integer(), primary_key=True)
  vehicle_id = db.Column(db.Integer(), nullable=False)
  vehicle_label = db.Column(db.Integer(255), nullable=True)
  vehicle_current_status = db.Column(db.Integer(), nullable=False)
  geographic_point = db.Column(db.String(255), nullable=False)
  position_speed = db.Column(db.Integer(), nullable=True)
  trip_schedule_relationship = db.Column(db.Integer(), nullable=True)
  trip_start_date = db.Column(db.Intger(), nullable=True)
  trip_route_id = db.Column(db.Integer(), nullable=True)
  trip_id = db.Column(db.Integer(), nullable=True)
  alcaldia_id = db.Column(db.Integer(), db.ForeignKey('Alcaldia.id'), nullable=True)
  created_at  = db.Column(db.TIMESTAMP, default=func.current_timestamp())
  updated_at = db.Column(db.TIMESTAMP)

  def __init__(self, id=0):
      self.id = id
  
  def serialize(self):
      return {
          'id': self.id,
          'vehicle_id': self.vehicle_id,
          'vehicle_label': self.vehicle_label,
          'vehicle_current_status': self.vehicle_current_status,
          'geographic_point': self.geographic_point,
          'trip_schedule_relationship': self.trip_schedule_relationship,
          'trip_start_date': self.trip_start_date,
          'trip_route_id': self.trip_route_id,
          'trip_id': self.trip_id,
          'alcaldia_id': self.alcaldia_id,
          'position_speed': self.position_speed,
          'created_at': str(self.created_at),
          'updated_at': str(self.updated_at)
      }
