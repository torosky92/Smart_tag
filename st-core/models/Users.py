from datetime import datetime

class Users:
    def __init__(self,
                 User_id: int,
                 company: str,
                 name: str,
                 lastname: str,
                 address: str,
                 city: str,
                 country: str,
                 code: str = '',
                 user: str,
                 password: str
                 ):
        self._name = name
        self._User_id= User_id
        self._company = company
        self._lastname = lastname
        self._address = address
        self._city = city
        self._country = country
        self._code = code
        self._user = user
        self._password = password

    def to_dict(self):
        return {
            'name':self._name,
            'user_id'=self._User_id,
            'company'=self._company,
            'lastname'=self._lastname,
            'address'=self._address,
            'city'=self._city,
            'country'=self._country,
            'code'=self._code,
            'user'=self._user,
            'password'=self._password
        }