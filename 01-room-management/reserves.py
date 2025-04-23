# reserves.py
"""
Aquest mòdul gestiona les reserves de l'hotel CalaGava.

Funcions:
- afegir_reserva: registra una reserva si l'habitació està disponible.
- mostrar_info_client: mostra la reserva associada a un DNI concret.
- mostrar_totes_les_reserves: mostra totes les reserves.

Les dades es desen i es llegeixen del fitxer `dades/reserves.txt`.
"""

import os

RUTA_RESERVES = "dades/reserves.txt"
RUTA_HABITACIONS = "dades/habitacions.txt"

def carregar_reserves():
    """
    Llegeix totes les reserves i les retorna com a llista de diccionaris.
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

def carregar_habitacions():
    """
    Llegeix les habitacions i les retorna com a llista de diccionaris.
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
    Guarda les habitacions al fitxer de text.
    """
    with open(RUTA_HABITACIONS, "w", encoding="utf-8") as f:
        for hab in habitacions:
            f.write(f"{hab['num']},{hab['capacitat']},{hab['estat']},{hab['preu']}\n")

def validar_dni(dni):
    return len(dni) == 9

def validar_telefon(telefon):
    return telefon.isdigit() and len(telefon) >= 9

def afegir_reserva(num, nom, cognom, dni, telefon):
    """
    Afegeix una reserva si l'habitació està disponible i les dades són vàlides.
    """
    if not validar_dni(dni):
        print("DNI no vàlid. Ha de tenir 9 caràcters.")
        return
    if not validar_telefon(telefon):
        print("Telèfon no vàlid. Només números i mínim 9 dígits.")
        return

    habitacions = carregar_habitacions()
    reserves = carregar_reserves()

    for hab in habitacions:
        if hab["num"] == num:
            if hab["estat"] != "disponible":
                print(f"L'habitació {num} no està disponible.")
                return
            else:
                # Canviem l'estat a "ocupada"
                hab["estat"] = "ocupada"
                nova_reserva = {
                    "habitacio": num,
                    "nom": nom,
                    "cognom": cognom,
                    "dni": dni,
                    "telefon": telefon
                }
                reserves.append(nova_reserva)
                guardar_reserves(reserves)
                guardar_habitacions(habitacions)
                print(f"Reserva realitzada correctament per a l'habitació {num}.")
                return

    print(f"No existeix cap habitació amb el número {num}.")

def mostrar_info_client(dni):
    """
    Mostra les reserves associades a un DNI.
    """
    reserves = carregar_reserves()
    trobades = [r for r in reserves if r["dni"] == dni]

    if not trobades:
        print("ℹNo hi ha reserves associades a aquest DNI.")
    else:
        print(f"Reserves del client amb DNI {dni}:")
        for r in trobades:
            print(f"  Habitació {r['habitacio']} - {r['nom']} {r['cognom']}, Telèfon: {r['telefon']}")

def mostrar_totes_les_reserves():
    """
    Mostra totes les reserves registrades.
    """
    reserves = carregar_reserves()
    if not reserves:
        print("ℹNo hi ha cap reserva registrada.")
    else:
        print("Totes les reserves:")
        for r in reserves:
            print(f"  Habitació {r['habitacio']} - {r['nom']} {r['cognom']}, DNI: {r['dni']}, Telèfon: {r['telefon']}")
