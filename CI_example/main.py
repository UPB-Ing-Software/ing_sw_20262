from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    var = "Hello World"
    var2 = "Hello FastAPI"
    var3 = var + " and " + var2
    return var3