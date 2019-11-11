from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class DBShelf(Base):
   __tablename__ = 'ESTANTE'
   ref = Column("Ref", int, primary_key=True)
   id = Column("Id", String)
   row = Column("Fila", String)
   column = Column("Columna", String)

   def FindShelf(TABLA: str, Reference: int):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      Ref = session.query(DBShelf).all()
      session.close()
      for References in Ref:
         if References.ref == Reference:
            return (References.id, References.row, References.column)

   def FindALLShelf(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      refe = session.query(DBShelf).all()
      session.close()
      New_id = []
      New_row = []
      New_column = []
      for References in refe:
         New_id.append(References.id)
         New_row.append(References.row)
         New_column.append(References.column)
      return (New_id, New_row, New_column)

   def AddShelf(TABLA: str, Id: str, Row: str, Col: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      Shelf = DBShelf()
      Shelf.id = Id
      Shelf.row = Row
      Shelf.column = Col
      session.add(Shelf)
      session.commit()
      session.close()

   def DeleteShelf(TABLA: str, Ref: int):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(DBShelf).filter_by(ref=Ref).delete()
      session.commit()
      session.close()

   def DeleteALLShelf(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(DBShelf).delete()
      session.commit()
      session.close()

   def UpdateShelf(TABLA: str, Reference: int, Data: str, Value: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if Data == "Id": session.query(DBShelf).filter_by(ref=Reference).update({DBShelf.id: Value})
      elif Data == "Fila": session.query(DBShelf).filter_by(ref=Reference).update({DBShelf.row: Value})
      elif Data == "Columna": session.query(DBShelf).filter_by(ref=Reference).update({DBShelf.column: Value})
      session.commit()
      session.close()

   def CreateShelf(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)