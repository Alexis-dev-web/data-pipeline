from app.alcaldia.controller.AlcaldiasController import AlcaldiasController


def create_routes(api):
  """
    General routes
  """
  api.add_resource(AlcaldiasController, '/apiV1/alcaldias')