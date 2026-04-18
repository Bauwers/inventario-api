from fastapi import FastAPI
from database import Producto, Session

app = FastAPI()


@app.get("/productos")
def obtener_productos():
    session = Session()
    productos = session.query(Producto).all()
    session.close()
    return productos


@app.post("/productos")
def agregar_productos(nombre: str, precio: float, stock: int):
    session = Session()
    producto = Producto(nombre=nombre, precio=precio, stock=stock)
    session.add(producto)
    session.commit()
    session.close()
    return {"mensaje": "Producto agregado"}


@app.get("/productos/{nombre}")
def buscar_producto(nombre: str):
    session = Session()
    producto = session.query(Producto).filter(Producto.nombre == nombre).first()
    session.close()
    if producto:
        return producto
    return {"error": "Producto no encontrado"}


@app.put("/productos/{nombre}")
def actualizar_producto(nombre: str, nuevo_stock: int):
    session = Session()
    producto = session.query(Producto).filter(Producto.nombre == nombre).first()
    if producto:
        producto.stock = nuevo_stock
        session.commit()
        session.close()
        return {"mensaje": "Stock actualizado"}
    return {"error": "Producto no encontrado, imposible actualizar"}


@app.delete("/productos/{nombre}")
def eliminar_producto(nombre: str):
    session = Session()
    producto = session.query(Producto).filter(Producto.nombre == nombre).first()
    if producto:
            session.delete(producto)
            session.commit()
            session.close()
            return {"mensaje": "Producto eliminado"}
    return {
        "mensaje": "Error, el producto no puede ser eliminado ya que no se encuentra"
    }
