from fastapi import FastAPI
from . import models, database, auth

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Flork API")

@app.get("/")
def root():
    return {"msg": "Bienvenido a la API de Flork"}

# Incluir rutas
app.include_router(auth.router)
