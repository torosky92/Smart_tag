from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
import json

Base = declarative_base()

class DBDisplay(Base):
   __tablename__ = 'Display'
   ref = Column("Ref", Integer, primary_key=True)
   tag_id = Column("Referencia Display", Integer)
   store = Column("Tienda", String)
   location = Column("Locacion", String)
   product = Column("Producto", Float)

   def FindTag(TABLA: str, ID_tag: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      DB = session.query(DBDisplay).all()
      session.close()
      for BaseData in DB:
         if BaseData.tag_id == ID_tag:
            location_json = json.dumps(BaseData.location)
            find_disp={"tag_id":BaseData.tag_id,"store":BaseData.store,
                        "location":location_json,"product":BaseData.product}
            find_json=json.dumps(find_disp)
            return find_json

   def FindALLTag(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      DB = session.query(DBDisplay).all()
      session.close()
      New_tag_id= []
      New_store = []
      New_location = []
      New_product = []
      for BaseData in DB:
         New_tag_id.append(BaseData.tag_id)
         New_store.append(BaseData.store)
         New_location.append(BaseData.location)
         New_product.append(BaseData.product)
      return (New_tag_id, New_store, New_location, New_product)

   def AddTag(TABLA: str, request: dict):
      display=json.loads(request)
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      DB = DBDisplay()
      DB.tag_id = display['tag_id']
      DB.store = display['store']
      DB.location = display['location']
      DB.product = display['product']
      session.add(DB)
      session.commit()
      session.close()

   def DeleteTag(TABLA: str, ID_tag: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(DBDisplay).filter_by(tag_id=ID_tag).delete()
      session.commit()
      session.close()

   def DeleteALLTag(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(DBDisplay).delete()
      session.commit()
      session.close()

   def UpdateTag(TABLA: str, ID_tag: str, DATA: str, Value: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      N_Table = DBDisplay
      if DATA == "tag_id": session.query(N_Table).filter_by(tag_id=ID_tag).update({DBDisplay.tag_id: Value})
      elif DATA == "store": session.query(N_Table).filter_by(tag_id=ID_tag).update({DBDisplay.store: Value})
      elif DATA == "location": session.query(N_Table).filter_by(tag_id=ID_tag).update({DBDisplay.location: Value})
      elif DATA == "product": session.query(N_Table).filter_by(tag_id=ID_tag).update({DBDisplay.product: Value})
      session.commit()
      session.close()

   def CreateTag(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)