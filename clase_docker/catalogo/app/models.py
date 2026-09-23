from sqlmodel import Field, SQLModel


class Articulo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    precio: float
