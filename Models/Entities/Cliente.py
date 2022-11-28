class Cliente():

    def __init__(self, cedula, nombre, apellido, correo, telefono):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono


    def toJSON(self):
        return {
            'cedula': self.cedula,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'correo': self.correo,
            'telefono': self.telefono
        }