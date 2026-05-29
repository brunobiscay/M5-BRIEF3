from fastapi import FastAPI, HTTPException
from loguru import logger
from modules.calcul import calcul_carre
from prometheus_fastapi_instrumentator import Instrumentator
from pydantic import BaseModel
from prometheus_client import Counter

calcul_counter = Counter(
    "calcul_requests_total",
    "Nombre total d'appels à /calcul"
)

# ✅ Configuration logs
logger.add(
    "main.log", format="{time} | {level} | {message}", level="INFO", rotation="1 MB"
)

app = FastAPI()

# ✅ Instrumentation Prometheus
Instrumentator().instrument(app).expose(app, endpoint="/metrics"))


class Nombre(BaseModel):
    valeur: int


@app.get("/")
def root():
    logger.info("Route '/' appelée")
    return {"message": "API en fonctionnement"}


@app.get("/health")
def health():
    logger.info("Route '/health' appelée")
    return {"status": "ok"}


@app.post("/calcul")
def calcul(nombre: Nombre):
    try:
        calcul_counter.inc()
        logger.info(f"Requête reçue: {nombre.valeur}")
        resultat = calcul_carre(nombre.valeur)
        return {"resultat": resultat}
    except Exception as e:
        logger.error(f"Erreur dans /calcul: {e}")
        raise HTTPException(status_code=400, detail=str(e))
