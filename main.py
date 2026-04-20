from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth import hashear_password, verificar_password, crear_token, verificar_token
from database import Producto, Session, Usuario

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.get("/productos")
def obtener_productos(token: str = Depends(oauth2_scheme)):
    usuario = verificar_token(token)
    if not usuario:
        raise HTTPException(status_code=401, detail="No autorizado")
    session = Session()
    productos = session.query(Producto).all()
    session.close()
    return productos


@app.post("/productos")
def agregar_productos(nombre: str, precio: float, stock: int, token: str = Depends(oauth2_scheme)):
    usuario = verificar_token(token)
    if not usuario:
        raise HTTPException(status_code=401, detail="No autorizado")
    session = Session()
    producto = Producto(nombre=nombre, precio=precio, stock=stock)
    session.add(producto)
    session.commit()
    session.close()
    return {"mensaje": "Producto agregado"}


@app.get("/productos/{nombre}")
def buscar_producto(nombre: str, token: str = Depends(oauth2_scheme)):
    usuario = verificar_token(token)
    if not usuario:
        raise HTTPException(status_code=401, detail="No autorizado")
    session = Session()
    producto = session.query(Producto).filter(Producto.nombre == nombre).first()
    session.close()
    if producto:
        return producto
    return {"error": "Producto no encontrado"}


@app.put("/productos/{nombre}")
def actualizar_producto(nombre: str, nuevo_stock: int, token: str = Depends(oauth2_scheme)):
    usuario = verificar_token(token)
    if not usuario:
        raise HTTPException(status_code=401, detail="No autorizado")
    session = Session()
    producto = session.query(Producto).filter(Producto.nombre == nombre).first()
    if producto:
        producto.stock = nuevo_stock
        session.commit()
        session.close()
        return {"mensaje": "Stock actualizado"}
    return {"error": "Producto no encontrado, imposible actualizar"}


@app.delete("/productos/{nombre}")
def eliminar_producto(nombre: str, token: str = Depends(oauth2_scheme)):
    usuario = verificar_token(token)
    if not usuario:
        raise HTTPException(status_code=401, detail="No autorizado")
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



@app.post("/registro")
def registro(username: str, password: str):
    session = Session()
    usuario_existente = session.query(Usuario).filter(Usuario.username == username).first()
    if usuario_existente:
        session.close()
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    nuevo_usuario = Usuario(username=username, password_hash=hashear_password(password))
    session.add(nuevo_usuario)
    session.commit()
    session.close()
    return {"mensaje": "Usuario registrado"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.username == form_data.username).first()
    session.close()
    if not usuario or not verificar_password(form_data.password, usuario.password_hash):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    token = crear_token({"sub": usuario.username})
    return {"access_token": token, "token_type": "bearer"}
