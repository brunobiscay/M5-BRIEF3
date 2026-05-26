from loguru import logger

# ✅ fichier dédié pour ce module
logger.add(
    "calcul.log", format="{time} | {level} | {message}", level="INFO", rotation="1 MB"
)


def calcul_carre(nombre: int) -> int:
    try:
        logger.info(f"Calcul du carré pour: {nombre}")
        resultat = nombre * nombre
        logger.info(f"Résultat: {resultat}")
        return resultat
    except Exception as e:
        logger.error(f"Erreur dans calcul_carre: {e}")
        raise
