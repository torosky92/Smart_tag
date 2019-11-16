from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
import json

Base = declarative_base()

class DBUser(Base):
   __tablename__ = 'Usuarios'
   ref = Column("Ref", Integer, primary_key=True)
   User = Column("Usuario", String)
   Password = Column("Contraseña", String)

   def FindUser(TABLA: str, Users: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      Ref = session.query(DBUser).all()
      session.close()
      for References in Ref:
         if References.User == Users:
            find_user={"user":BaseData.User,"password":BaseData.Password}
      find_user={"user":"","password":""}
      find_json=json.dumps(find_user)
      return find_json

   def FindALLUser(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      Ref = session.query(DBUser).all()
      session.close()
      New_User = []
      New_Password = []
      for References in Ref:
         New_User.append(References.User)
         New_Password.append(References.Password)
      return (New_User, New_Password)

   def AddUser(TABLA: str, request: dict):
      users=json.loads(request.body.read().decode("utf-8"))
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      Db = DBUser()
      Db.User = users['user']
      Db.Password = users['password']
      session.add(Db)
      session.commit()
      session.close()

   def DeleteUser(TABLA: str, USER: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(DBUser).filter_by(User=USER).delete()
      session.commit()
      session.close()

   def DeleteALLUser(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(DBUser).delete()
      session.commit()
      session.close()

   def UpdateUser(TABLA: str, USER: str, Data: str, Value: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if Data == "User": session.query(DBUser).filter_by(User=USER).update({DBUser.User: Value})
      elif Data == "Password": session.query(DBUser).filter_by(User=USER).update({DBUser.Password: Value})
      session.commit()
      session.close()

   def CreateUser(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)