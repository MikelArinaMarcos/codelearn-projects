# main.py
"""
Aquest fitxer és el punt d'entrada del programa.
Llegeix els arguments passats per línia de comandes i crida les funcions dels mòduls corresponents.
"""

import sys
from habitacions import afegir_habitacio, finalitzar_estada, netejar_habitacio, mostrar_llista_habitacions
from reserves import afegir_reserva, mostrar_info_client, mostrar_totes_les_reserves

def mostrar_ajuda():
    print("Comandes disponibles:")
    print("  afegir habitacio <num> <capacitat> <preu>")
    print("  afegir reserva <num> <nom> <cognom> <dni> <telefon>")
    print("  finalitzar habitacio <num_dies>")
    print("  netejar habitacio")
    print("  list")
    print("  info <dni>")
    print("  reserves")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️ Error: No s'ha especificat cap comanda.")
        mostrar_ajuda()
        sys.exit(1)

    comanda = sys.argv[1]

    if comanda == "afegir":
        if len(sys.argv) < 3:
            print("⚠️ Error: Comanda 'afegir' incompleta.")
            mostrar_ajuda()
        elif sys.argv[2] == "habitacio" and len(sys.argv) == 6:
            afegir_habitacio(sys.argv[3], sys.argv[4], sys.argv[5])
        elif sys.argv[2] == "reserva" and len(sys.argv) == 8:
            afegir_reserva(sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
        else:
            print("⚠️ Error en la comanda 'afegir'. Revisa els paràmetres.")
            mostrar_ajuda()

    elif comanda == "finalitzar" and len(sys.argv) == 4 and sys.argv[2] == "habitacio":
        finalitzar_estada(sys.argv[3])

    elif comanda == "netejar" and len(sys.argv) == 3 and sys.argv[2] == "habitacio":
        netejar_habitacio()

    elif comanda == "list":
        mostrar_llista_habitacions()

    elif comanda == "info" and len(sys.argv) == 3:
        mostrar_info_client(sys.argv[2])

    elif comanda == "reserves":
        mostrar_totes_les_reserves()

    else:
        print("Comanda desconeguda o mal escrita.")
        mostrar_ajuda()
