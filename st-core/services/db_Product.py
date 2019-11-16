from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
import json

Base = declarative_base()

class DBProduct(Base):
   __tablename__ = 'Productos'
   ref = Column("Ref", Integer, primary_key=True)
   name = Column("Producto", String)
   price = Column("Precio", Float)
   quantity = Column("Cantidad", Integer)
   expiration = Column("Fecha de Caducidad", String)
   product_id = Column("Código de Barras", Integer)
   discount = Column("Descuento", Float)
   description = Column("Descripcion", String)

   def FindProduct(TABLA: str, name_Product: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      DB = session.query(DBProduct).all()
      session.close()
      for BaseData in DB:
         if BaseData.name == name_Product:
            find_prod={"product_id":BaseData.product_id,"name":BaseData.name,"price":BaseData.price,
                     "discount":BaseData.discount,"quantity":BaseData.quantity,"expiration":BaseData.expiration,"description":BaseData.description}
            find_json=json.dumps(find_prod)
            return find_json         
      find_prod={"product_id":0,"name":"","price":0, "discount":0,"quantity":0,"expiration":"","description":""}
      find_json=json.dumps(find_prod)
      return find_json

   def FindALLProduct(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      DB = session.query(DBProduct).all()
      session.close()
      New_product_id = []
      New_name = []
      New_price = []
      New_quantity = []
      New_expiration = []
      New_discount = []
      New_description = []
      for BaseData in DB:
         New_product_id.append(BaseData.product_id)
         New_name.append(BaseData.name)
         New_price.append(BaseData.price)
         New_quantity.append(BaseData.discount)
         New_expiration.append(BaseData.quantity)
         New_discount.append(BaseData.expiration)
         New_description.append(BaseData.description)
      return (New_product_id, New_name, New_price, New_quantity, New_expiration, New_discount, New_description)

   def AddProduct(TABLA: str, request: dict):
      product=json.loads(request.body.read().decode("utf-8"))
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      DB = DBProduct()
      DB.name = product['name']
      DB.price = product['price']
      DB.quantity = product['quantity']
      DB.expiration = product['expiration']
      DB.product_id = product['product_id']
      DB.discount = product['discount']
      DB.description = product['description']
      session.add(DB)
      session.commit()
      session.close()

   def DeleteProduct(TABLA: str, PRODUCT: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(DBProduct).filter_by(name=PRODUCT).delete()
      session.commit()
      session.close()

   def DeleteALLProduct(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(DBProduct).delete()
      session.commit()
      session.close()

   def UpdateProduct(TABLA: str, PRODUCT: str, DATA: str, Value: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      N_Table = DBProduct
      if DATA == "product_id": session.query(N_Table).filter_by(name=PRODUCT).update({DBProduct.product_id: Value})
      elif DATA == "name": session.query(N_Table).filter_by(name=PRODUCT).update({DBProduct.name: Value})
      elif DATA == "price": session.query(N_Table).filter_by(name=PRODUCT).update({DBProduct.price: Value})
      elif DATA == "quantity": session.query(N_Table).filter_by(name=PRODUCT).update({DBProduct.quantity: Value})
      elif DATA == "expiration": session.query(N_Table).filter_by(name=PRODUCT).update({DBProduct.expiration: Value})
      elif DATA == "discount": session.query(N_Table).filter_by(name=PRODUCT).update({DBProduct.discount: Value})
      elif DATA == "description": session.query(N_Table).filter_by(name=PRODUCT).update({DBProduct.description: Value})
      session.commit()
      session.close()

   def CreateProduct(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)