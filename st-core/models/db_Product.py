from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()
class Template1(object):
   ref = Column("Ref", int, primary_key=True)
   Product = Column("Producto", String)
   Price = Column("Precio", String)
   Discount = Column("Descuento", String)
   Quantity = Column("Cantidad", String)
   Data = Column("Fecha de Caducidad", String)
   Code = Column("Código de Barras", String)

class Template2(object):
   ref = Column("Ref", int, primary_key=True)
   Product = Column("Producto", String)
   Price = Column("Precio", String)
   Discount = Column("Descuento", String)
   Quantity = Column("Cantidad", String)
   Data = Column("Fecha Vendido", String)
   Code = Column("Código de Barras", String)

class DBProduct(Template1, Base):
   __tablename__ = 'Productos'

class DBProductSell(Template2, Base):
   __tablename__ = 'Productos Vendidos'

class DB_PROD(Base):  

   def FindProduct(NameTable: str, TABLA: str, New_Product: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      DB = session.query(DB_PROD.WhichTable(NameTable)).all()
      session.close()
      for BaseData in DB:
         if BaseData.Product == New_Product:
            return (BaseData.Product, BaseData.Price, BaseData.Discount, BaseData.Quantity, BaseData.Data, BaseData.Code)

   def FindALLProduct(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      DB = session.query(DB_PROD.WhichTable(NameTable)).all()
      session.close()
      New_Product = []
      New_Price = []
      New_Discount = []
      New_Quantity = []
      New_Data = []
      New_Code = []
      for BaseData in DB:
         New_Product.append(BaseData.Product)
         New_Price.append(BaseData.Price)
         New_Discount.append(BaseData.Discount)
         New_Quantity.append(BaseData.Quantity)
         New_Data.append(BaseData.Data)
         New_Code.append(BaseData.Code)
      return (New_Product, New_Price, New_Discount, New_Quantity, New_Data, New_Code)

   def AddProduct(NameTable: str, TABLA: str, PRODUCT: str, PRICE: str, DISCOUNT: str, QUANTITY: str, DATA: str, CODE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      if NameTable == "Product":  DB = DBProduct()
      elif NameTable == "ProductSell": DB = DBProductSell()
      DB.Product = PRODUCT
      DB.Price = PRICE
      DB.Discount = DISCOUNT
      DB.Quantity = QUANTITY
      DB.Data = DATA
      DB.Code = CODE
      session.add(DB)
      session.commit()
      session.close()

   def DeleteProduct(NameTable: str, TABLA: str, PRODUCT: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(DB_PROD.WhichTable(NameTable)).filter_by(Product=PRODUCT).delete()
      session.commit()
      session.close()

   def DeleteALLProduct(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(DB_PROD.WhichTable(NameTable)).delete()
      session.commit()
      session.close()

   def UpdateProduct(NameTable: str, TABLA: str, PRODUCT: str, DATA: str, Value: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      N_Table = DB_PROD.WhichTable(NameTable)
      if DATA == "Product": session.query(N_Table).filter_by(Product=PRODUCT).update({DBProduct.Product: Value})
      elif DATA == "Price": session.query(N_Table).filter_by(Product=PRODUCT).update({DBProduct.Price: Value})
      elif DATA == "Discount": session.query(N_Table).filter_by(Product=PRODUCT).update({DBProduct.Discount: Value})
      elif DATA == "Quantity": session.query(N_Table).filter_by(Product=PRODUCT).update({DBProduct.Quantity: Value})
      elif DATA == "Data": session.query(N_Table).filter_by(Product=PRODUCT).update({DBProduct.Data: Value})
      elif DATA == "Code": session.query(N_Table).filter_by(Product=PRODUCT).update({DBProduct.Code: Value})
      session.commit()
      session.close()

   def CreateProduct(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Table = DB_PROD.WhichTable(NameTable)
      Table.metadata.create_all(engine)
   
   def WhichTable(NameTable: str):
      if NameTable == "Product": return DBProduct
      elif NameTable == "ProductSell": return DBProductSell