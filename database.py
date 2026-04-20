from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///inventario.db")

Base = declarative_base()

class Producto(Base):
    __tablename__ = "productos"
    nombre = Column(String, primary_key=True)
    precio = Column(Float)
    stock = Column(Integer)
    
class Usuario(Base):
    __tablename__ = "usuarios"
    username = Column(String, primary_key=True)
    password_hash = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)