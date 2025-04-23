# habitacions.py
"""
Aquest mòdul gestiona les habitacions de l'hotel CalaGava.

Funcions:
- afegir_habitacio: afegeix una nova habitació al fitxer.
- finalitzar_estada: calcula el preu total i marca l'habitació com a "bruta" o "disponible".
- netejar_habitacio: canvia l'estat de l'habitació a "disponible" si estava bruta.
- mostrar_llista_habitacions: imprimeix totes les habitacions amb les seves dades.

Les dades es desen i es llegeixen del fitxer `dades/habitacions.txt`.
"""

import os

RUTA = "dades/habitacions.txt"

def carregar_habitacions():
    """
    Llegeix totes les habitacions del fitxer i les retorna com a llista.
    """
    habitacions = []
    if not os.path.exists(RUTA):
        return habitacions

    with open(RUTA, "r", encoding="utf-8") as f:
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
    with open(RUTA, "w", encoding="utf-8") as f:
        for hab in habitacions:
            f.write(f"{hab['num']},{hab['capacitat']},{hab['estat']},{hab['preu']}\n")

def afegir_habitacio(num, capacitat, preu):
    """
    Afegeix una nova habitació al sistema. Està disponible per defecte.
    """
    if int(num) < 1:
        print("Error: El número d'habitació ha de ser >= 1.")
        return

    habitacions = carregar_habitacions()
    for hab in habitacions:
        if hab["num"] == num:
            print("Error: Aquesta habitació ja existeix.")
            return

    nova = {
        "num": num,
        "capacitat": int(capacitat),
        "estat": "disponible",
        "preu": float(preu)
    }
    habitacions.append(nova)
    guardar_habitacions(habitacions)
    print(f"Habitació {num} afegida correctament.")

def finalitzar_estada(num_dies):
    """
    Finalitza una estada i marca l'habitació com a bruta o disponible segons els dies.
    """
    habitacions = carregar_habitacions()
    trobada = False

    for hab in habitacions:
        if hab["estat"] == "ocupada":
            trobada = True
            if int(num_dies) == 0:
                hab["estat"] = "disponible"
                print("ℹEstada anul·lada. No s'ha cobrat res.")
            else:
                total = int(num_dies) * hab["preu"]
                hab["estat"] = "bruta"
                print(f"Preu total de l'estada: {total:.2f} €")
            break

    if not trobada:
        print("No hi ha cap habitació ocupada per finalitzar.")
    else:
        guardar_habitacions(habitacions)

def netejar_habitacio():
    """
    Canvia l'estat d'una habitació bruta a disponible.
    """
    habitacions = carregar_habitacions()
    canviat = False

    for hab in habitacions:
        if hab["estat"] == "bruta":
            hab["estat"] = "disponible"
            canviat = True
            print(f"Habitació {hab['num']} netejada i ara disponible.")
            break

    if not canviat:
        print("No hi ha habitacions brutes per netejar.")
    else:
        guardar_habitacions(habitacions)

def mostrar_llista_habitacions():
    """
    Mostra totes les habitacions amb la seva informació.
    """
    habitacions = carregar_habitacions()
    if not habitacions:
        print("No hi ha habitacions registrades.")
    else:
        print("Llista d'habitacions:")
        for hab in habitacions:
            print(f"  Habitació {hab['num']}: Capacitat {hab['capacitat']}, Estat {hab['estat']}, Preu {hab['preu']} €/dia")
