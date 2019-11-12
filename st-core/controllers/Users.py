from services.db_Users import DBUser
import settings
import json


class UserController:

    @staticmethod
    def verificate(request: dict):
        users = json.loads(request)
        user_db = DBUser.FindUser('sqlite:///entidades/DB.db',users['user'])
        user_json = json.loads(user_db)
        if users['user']==user_json['user']:
            if users['password']==user_json['password']:
                return True #Falta enviar al html
        return False #Falta enviar al html
    
    def update(request: dict):
        users = json.loads(request)
        DBUser.AddUser('sqlite:///entidades/DB.db',users)
    
    def delete(request: dict):
        users = json.loads(request)
        DBUser.DeleteUser('sqlite:///entidades/DB.db',users['user'])
