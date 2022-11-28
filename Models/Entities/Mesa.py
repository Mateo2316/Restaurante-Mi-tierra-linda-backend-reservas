class Mesa():

    def __init__(self, numero_mesa, capacidad):
        self.numero_mesa = numero_mesa
        self.capacidad = capacidad

    def toJSON(self):
        return {
            'numero_mesa': self.numero_mesa,
            'capacidad': self.capacidad
        }