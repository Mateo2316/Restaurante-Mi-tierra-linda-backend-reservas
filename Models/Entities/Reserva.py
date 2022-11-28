from Utils.DateFormat import DateFormat

class Reserva():

    def __init__(self, id_reserva, cedula, id_solicitud, numero_mesa, numero_asistentes, fecha, hora):
        self.id_reserva = id_reserva
        self.cedula = cedula
        self.id_solicitud = id_solicitud
        self.numero_mesa = numero_mesa
        self.numero_asistentes = numero_asistentes
        self.fecha = fecha
        self.hora = hora

    def toJSON(self):
        return {
            'id_reserva': self.id_reserva,
            'cedula': self.cedula,
            'id_solicitud': self.id_solicitud,
            'numero_mesa': self.numero_mesa,
            'numero_asistentes': self.numero_asistentes,
            'fecha': DateFormat.convertDate(self.fecha),
            'hora': str(self.hora)
        }

