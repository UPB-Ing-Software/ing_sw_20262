## Arranque local

```bash
uv sync
uv run uvicorn api.main:app --port 8080
```

`uv sync` crea el entorno `.venv` junto a `pyproject.toml` e instala las versiones exactas que fija `uv.lock`. `uv run` ejecuta el comando dentro de ese entorno sin activarlo.

`requirements.txt` lista esas mismas versiones para quien instale con `pip`, que no lee `uv.lock`.

- Health: `http://127.0.0.1:8080/health`
- Motor de base de datos en uso: `http://127.0.0.1:8080/info`

Por defecto persiste en `incidencias.db` (SQLite). Para apuntar a otro motor, define `DATABASE_URL` antes de arrancar.
