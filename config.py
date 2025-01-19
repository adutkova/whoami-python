import os

class Config:
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://') if os.environ.get('DATABASE_URL') else 'sqlite:///:memory:'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  
  # Map center coordinates
  MAP_CENTER = [50.0883,18.4124]

  # Default map zoom, range 0-18
  MAP_ZOOM = 3
