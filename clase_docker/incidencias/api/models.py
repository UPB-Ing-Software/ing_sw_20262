from sqlmodel import Field, SQLModel


class Incidencia(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titulo: str
    prioridad: int
