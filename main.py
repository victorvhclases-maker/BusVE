# main.py
from billete import Billete

def main():
    
    plazas_max = 50
    matricula = "ABC123"

    sistema = Billete(plazas_max, matricula)

    while True:
        print("\n--- MENÚ ---")
        print("1.- Venta de billetes.")
        print("2.- Devolución de billetes.")
        print("3.- Estado de la venta.")
        print("0.- Salir.")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            total, libres, vendidas = sistema.venta_billete()
            print(f"Estado -> Total: {total} | Libre: {libres} | Vendido: {vendidas}")

        elif opcion == "2":
            total, libres, vendidas = sistema.devolucion()
            print(f"Estado -> Total: {total} | Libre: {libres} | Vendido: {vendidas}")

        elif opcion == "3":
            total, libres, vendidas = sistema.estado()
            print("Estado de la venta")
            print(f"Total: {total}")
            print(f"Libre: {libres}")
            print(f"Vendido: {vendidas}")

        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
