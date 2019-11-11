from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class DBSug(Base):
   __tablename__ = 'Sugerencias'
   ref = Column("Ref", int, primary_key=True)
   Company = Column("Compañia", String)
   Name = Column("Nombres", String)
   LastName = Column("Apellidos", String)
   Address = Column("Dirección", String)
   City = Column("Ciudad", String)
   Country = Column("Pais", String)
   Code = Column("Código Postal", String)
   Affair = Column("Asunto", String)
   Suggestion = Column("Sugerencia o Cotización", String)

   def FindSug(TABLA: str, Reference: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      Ref = session.query(DBSug).all()
      session.close()
      for References in Ref:
         if References.ref == Reference:
            return (References.Company, References.Name, References.LastName, References.Address, References.City, References.Country, References.Code, References.Affair, References.Password)

   def FindALLSug(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      Ref = session.query(DBSug).all()
      session.close()
      New_Company = []
      New_Name = []
      New_LastName = []
      New_Address = []
      New_City = []
      New_Country = []
      New_Code = []
      New_Affair = []
      New_Suggestion = []
      for References in Ref:
         New_Company.append(References.Company)
         New_Name.append(References.Name)
         New_LastName.append(References.LastName)
         New_Address.append(References.Address)
         New_City.append(References.City)
         New_Country.append(References.Country)
         New_Code.append(References.Code)
         New_Affair.append(References.Affair)
         New_Password.append(References.Suggestion)
      return (New_Company, New_Name, New_LastName, New_Address, New_City, New_Country, New_Code, New_Affair, New_Suggestion)

   def AddSug(TABLA: str, COMPANY: str, NAME: str, LASTNAME: str, ADDRESS: str,
             CITY: str, COUNTRY: str, CODE: str, AFFAIR: str, SUGGESTION: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      Db = DBSug()
      Db.Company = COMPANY
      Db.Name = NAME
      Db.LastName = LASTNAME
      Db.Address = ADDRESS
      Db.City = CITY
      Db.Country = COUNTRY
      Db.Code = CODE
      Db.Affair = AFFAIR
      Db.Suggestion = PASSWORD
      session.add(Db)
      session.commit()
      session.close()

   def DeleteSug(TABLA: str, NAME: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(DBSug).filter_by(Name=NAME).delete()
      session.commit()
      session.close()

   def DeleteALLSug(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(DBSug).delete()
      session.commit()
      session.close()

   def UpdateSug(TABLA: str, NAME: str, Data: str, Value: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if Data == "Company": session.query(DBSug).filter_by(Name=NAME).update({DBSug.Company: Value})
      elif Data == "Name": session.query(DBSug).filter_by(Name=NAME).update({DBSug.Name: Value})
      elif Data == "LastName": session.query(DBSug).filter_by(Name=NAME).update({DBSug.LastName: Value})
      elif Data == "Address": session.query(DBSug).filter_by(Name=NAME).update({DBSug.Address: Value})
      elif Data == "City": session.query(DBSug).filter_by(Name=NAME).update({DBSug.City: Value})
      elif Data == "Country": session.query(DBSug).filter_by(Name=NAME).update({DBSug.Country: Value})
      elif Data == "Code": session.query(DBSug).filter_by(Name=NAME).update({DBSug.Code: Value})
      elif Data == "Affair": session.query(DBSug).filter_by(Name=NAME).update({DBSug.Affair: Value})
      elif Data == "Suggestion": session.query(DBSug).filter_by(Name=NAME).update({DBSug.Suggestion: Value})
      session.commit()
      session.close()

   def CreateSug(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)