from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlmodel import Session, select

from app.db import crear_tablas, get_session
from app.models import Articulo


@asynccontextmanager
async def lifespan(app: FastAPI):
    crear_tablas()
    yield


app = FastAPI(title="Catálogo", lifespan=lifespan)


@app.get("/health")
def health():
    return {"estado": "ok"}


@app.get("/articulos")
def listar_articulos(session: Session = Depends(get_session)):
    return session.exec(select(Articulo)).all()


@app.post("/articulos")
def crear_articulo(articulo: Articulo, session: Session = Depends(get_session)):
    session.add(articulo)
    session.commit()
    session.refresh(articulo)
    return articulo
