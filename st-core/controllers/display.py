from services.db_Display import DBDisplay
import settings
import json

class DisplayController:
    @staticmethod
    def verificate(request: dict):
        display = json.loads(request)
        display_db = DBDisplay.FindTag('sqlite:///entidades/DB.db',display['tag_id'])
        display_json = json.loads(display_db)
        return display_json #Falta enviar al html

    def add(request: dict):
        display = json.loads(request)
        DBDisplay.AddTag('sqlite:///entidades/DB.db',display)
    
    def update(request: dict):
        display = json.loads(request)
        display_db = DBDisplay.FindTag('sqlite:///entidades/DB.db',display['tag_id'])
        display_json = json.loads(display_db)
        if display['tag_id']==display_json['tag_id']:
            if display['store']!=display_json['store']:
                DBDisplay.UpdateTag('sqlite:///entidades/DB.db',display['tag_id'],'store',display['store'])
            if display['location']!=display_json['location']:
                DBDisplay.UpdateTag('sqlite:///entidades/DB.db',display['tag_id'],'location',display['location'])
            if display['product']!=display_json['product']:
                DBDisplay.UpdateTag('sqlite:///entidades/DB.db',display['tag_id'],'product',display['product'])
        else:
            DisplayController.add(display)
    
    def delet(request: dict):
        display = json.loads(request)
        DBDisplay.DeleteTag('sqlite:///entidades/DB.db',display['tag_id'])



