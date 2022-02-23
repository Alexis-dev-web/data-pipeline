from flask import request
from flask.json import jsonify
from flask_restful import Resource

from app import app
from app.alcaldia.service.AlcaldiaService import AlcaldiaService


class AlcaldiasController(Resource):

  def __init__(self):
    self.alcaldiaService = AlcaldiaService()

  def get(self):
    app.logger.info(f"AlcaldiasController#get START - Request recieved - userAgent={request.user_agent.string}")
            
    alcaldias = self.alcaldiaService.get_all()

    app.logger.info(f"AlcaldiasController#get SUCCESS - Get all alcaldias - totalAlcaldias={len(alcaldias)}")

    return jsonify(data=alcaldias)
