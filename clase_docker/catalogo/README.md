
## Arranque local

```bash
uv sync
uv run uvicorn app.main:app --port 8000
```

`uv sync` crea el entorno `.venv` junto a `pyproject.toml` e instala las versiones exactas que fija `uv.lock`. `uv run` ejecuta el comando dentro de ese entorno sin activarlo, así que los mismos comandos funcionan en Linux, macOS y Windows.

`requirements.txt` lista esas mismas versiones para quien instale con `pip`, que no lee `uv.lock`. Se regenera tras cambiar una dependencia con `uv export --no-hashes --no-emit-project --format requirements-txt -o requirements.txt`.

- Health: `http://127.0.0.1:8000/health`

Por defecto persiste en `catalogo.db` (SQLite). Para apuntar a otro motor, define `DATABASE_URL` antes de arrancar.
