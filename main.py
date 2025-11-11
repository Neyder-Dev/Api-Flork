from fastapi import FastAPI
from . import models, database, auth
import auth, recetas 

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Flork API")

@app.get("/")
def root():
    return {"msg": "Bienvenido a la API de Flork"}

app.include_router(auth.router)
app.include_router(recetas.router)  

