class Solicitud():

    def __init__(self, id, tipo, descripcion, valor):
        self.id = id
        self.tipo = tipo
        self.descripcion = descripcion
        self.valor = valor

    def toJSON(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'descripcion': self.descripcion,
            'valor': self.valor,
        }