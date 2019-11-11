from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class DBUser(Base):
   __tablename__ = 'Usuarios'
   ref = Column("Ref", int, primary_key=True)
   Company = Column("Compañia", String)
   Name = Column("Nombres", String)
   LastName = Column("Apellidos", String)
   Address = Column("Dirección", String)
   City = Column("Ciudad", String)
   Country = Column("Pais", String)
   Code = Column("Código Postal", String)
   User = Column("Usuario", String)
   Password = Column("Contraseña", String)

   def FindUser(TABLA: str, Reference: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      Ref = session.query(DBUser).all()
      session.close()
      for References in Ref:
         if References.ref == Reference:
            return (References.Company, References.Name, References.LastName, References.Address, References.City, References.Country, References.Code, References.User, References.Password)

   def FindALLUser(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      Ref = session.query(DBUser).all()
      session.close()
      New_Company = []
      New_Name = []
      New_LastName = []
      New_Address = []
      New_City = []
      New_Country = []
      New_Code = []
      New_User = []
      New_Password = []
      for References in Ref:
         New_Company.append(References.Company)
         New_Name.append(References.Name)
         New_LastName.append(References.LastName)
         New_Address.append(References.Address)
         New_City.append(References.City)
         New_Country.append(References.Country)
         New_Code.append(References.Code)
         New_User.append(References.User)
         New_Password.append(References.Password)
      return (New_Company, New_Name, New_LastName, New_Address, New_City, New_Country, New_Code, New_User, New_Password)

   def AddUser(TABLA: str, COMPANY: str, NAME: str, LASTNAME: str, ADDRESS: str,
             CITY: str, COUNTRY: str, CODE: str, USER: str, PASSWORD: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      Db = DBUser()
      Db.Company = COMPANY
      Db.Name = NAME
      Db.LastName = LASTNAME
      Db.Address = ADDRESS
      Db.City = CITY
      Db.Country = COUNTRY
      Db.Code = CODE
      Db.User = USER
      Db.Password = PASSWORD
      session.add(Db)
      session.commit()
      session.close()

   def DeleteUser(TABLA: str, NAME: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(DBUser).filter_by(Name=NAME).delete()
      session.commit()
      session.close()

   def DeleteALLUser(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(DBUser).delete()
      session.commit()
      session.close()

   def UpdateUser(TABLA: str, NAME: str, Data: str, Value: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if Data == "Company": session.query(DBUser).filter_by(Name=NAME).update({DBUser.Company: Value})
      elif Data == "Name": session.query(DBUser).filter_by(Name=NAME).update({DBUser.Name: Value})
      elif Data == "LastName": session.query(DBUser).filter_by(Name=NAME).update({DBUser.LastName: Value})
      elif Data == "Address": session.query(DBUser).filter_by(Name=NAME).update({DBUser.Address: Value})
      elif Data == "City": session.query(DBUser).filter_by(Name=NAME).update({DBUser.City: Value})
      elif Data == "Country": session.query(DBUser).filter_by(Name=NAME).update({DBUser.Country: Value})
      elif Data == "Code": session.query(DBUser).filter_by(Name=NAME).update({DBUser.Code: Value})
      elif Data == "User": session.query(DBUser).filter_by(Name=NAME).update({DBUser.User: Value})
      elif Data == "Password": session.query(DBUser).filter_by(Name=NAME).update({DBUser.Password: Value})
      session.commit()
      session.close()

   def CreateUser(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)