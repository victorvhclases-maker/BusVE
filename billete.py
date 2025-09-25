# billete.py
from bus import Bus

class Billete:

    def __init__(self, plazas_max: int, matricula: str):
        self.bus = Bus(plazas_max, matricula)

    def venta_billete(self):
        try:
            tickets = int(input("¿Cuántos billetes quieres comprar? "))
        except ValueError:
            print("Entrada inválida. Debes introducir un número entero.")
            return self.estado()

        ok, msg = self.bus.vender_plazas(tickets)
        print(msg)
        return self.estado()

    def devolucion(self):
        try:
            tickets = int(input("¿Cuántos billetes quieres devolver? "))
        except ValueError:
            print("Entrada inválida. Debes introducir un número entero.")
            return self.estado()

        ok, msg = self.bus.devolver_plazas(tickets)
        print(msg)
        return self.estado()

    def estado(self):
        total = self.bus.plazas_max
        libres = self.bus.plazas_libres
        vendidas = self.bus.plazas_vendidas
        return total, libres, vendidas
