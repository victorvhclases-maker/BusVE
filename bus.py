
class Bus:
    def __init__(self, plazas_max, matricula):
        self.plazas_max = plazas_max
        self.matricula = matricula
        self.plazas_vendidas = 0

    @property
    def plazas_libres(self):
        """Devuelve las plazas libres disponibles en el bus."""
        return self.plazas_max - self.plazas_vendidas

    def vender_plazas(self, cantidad):
        """Vende una cantidad de plazas si hay disponibles."""
        if cantidad <= 0:
            return False, "La cantidad debe ser mayor que 0."
        if cantidad <= self.plazas_libres:
            self.plazas_vendidas += cantidad
            return True, f"Se vendieron {cantidad} plaza(s)."
        else:
            return False, f"No hay suficientes plazas. Libres: {self.plazas_libres}"

    def devolver_plazas(self, cantidad):
        """Devuelve una cantidad de plazas si no excede lo vendido."""
        if cantidad <= 0:
            return False, "La cantidad debe ser mayor que 0."
        if cantidad <= self.plazas_vendidas:
            self.plazas_vendidas -= cantidad
            return True, f"Se devolvieron {cantidad} plaza(s)."
        else:
            return False, f"No puedes devolver más de las vendidas ({self.plazas_vendidas})."
