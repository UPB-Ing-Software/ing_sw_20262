from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlmodel import Session, select

from api.db import crear_tablas, engine, get_session
from api.models import Incidencia


@asynccontextmanager
async def lifespan(app: FastAPI):
    crear_tablas()
    yield


app = FastAPI(title="Incidencias", lifespan=lifespan)


@app.get("/health")
def health():
    return {"estado": "ok"}


@app.get("/info")
def info():
    return {"motor": engine.dialect.name}


@app.get("/incidencias")
def listar_incidencias(session: Session = Depends(get_session)):
    return session.exec(select(Incidencia)).all()


@app.post("/incidencias")
def crear_incidencia(incidencia: Incidencia, session: Session = Depends(get_session)):
    session.add(incidencia)
    session.commit()
    session.refresh(incidencia)
    return incidencia
