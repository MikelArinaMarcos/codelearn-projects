# fitxers.py
"""
Aquest mòdul centralitza la gestió dels fitxers del sistema.

Funcions:
- carregar_habitacions / guardar_habitacions
- carregar_reserves / guardar_reserves

Tots els fitxers es guarden dins la carpeta `dades/`
"""

import os

RUTA_HABITACIONS = "dades/habitacions.txt"
RUTA_RESERVES = "dades/reserves.txt"

def carregar_habitacions():
    """
    Llegeix les habitacions des del fitxer i retorna una llista de diccionaris.
    """
    habitacions = []
    if not os.path.exists(RUTA_HABITACIONS):
        return habitacions

    with open(RUTA_HABITACIONS, "r", encoding="utf-8") as f:
        for linia in f:
            parts = linia.strip().split(",")
            if len(parts) == 4:
                habitacions.append({
                    "num": parts[0],
                    "capacitat": int(parts[1]),
                    "estat": parts[2],
                    "preu": float(parts[3])
                })
    return habitacions

def guardar_habitacions(habitacions):
    """
    Escriu la llista d'habitacions al fitxer.
    """
    with open(RUTA_HABITACIONS, "w", encoding="utf-8") as f:
        for hab in habitacions:
            f.write(f"{hab['num']},{hab['capacitat']},{hab['estat']},{hab['preu']}\n")

def carregar_reserves():
    """
    Llegeix les reserves des del fitxer i retorna una llista de diccionaris.
    """
    reserves = []
    if not os.path.exists(RUTA_RESERVES):
        return reserves

    with open(RUTA_RESERVES, "r", encoding="utf-8") as f:
        for linia in f:
            parts = linia.strip().split(",")
            if len(parts) == 5:
                reserves.append({
                    "habitacio": parts[0],
                    "nom": parts[1],
                    "cognom": parts[2],
                    "dni": parts[3],
                    "telefon": parts[4]
                })
    return reserves

def guardar_reserves(reserves):
    """
    Escriu la llista de reserves al fitxer.
    """
    with open(RUTA_RESERVES, "w", encoding="utf-8") as f:
        for r in reserves:
            f.write(f"{r['habitacio']},{r['nom']},{r['cognom']},{r['dni']},{r['telefon']}\n")
