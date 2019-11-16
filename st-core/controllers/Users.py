from services.db_Users import DBUser
import settings
import json


class UserController:

    @staticmethod
    def verificate(request: dict):
        users = json.loads(request.body.read().decode("utf-8"))
        user_db = DBUser.FindUser('sqlite:///entidades/DB.db',users['user'])
        user_json = json.loads(user_db)
        if users['user']==user_json['user']:
            if users['password']==user_json['password']:
                return True 
        return False
    
    def update(request: dict):
        DBUser.AddUser('sqlite:///entidades/DB.db',users)
    
    def delete(request: dict):
        users = json.loads(request.body.read().decode("utf-8"))
        DBUser.DeleteUser('sqlite:///entidades/DB.db',users['user'])
