from Database.db import getConnection
from .Entities.Reserva import Reserva

class ReservaModel():

    @classmethod
    def getReservas(self):
        try:
            connection = getConnection()
            reservas = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM reserva")
                resulset = cursor.fetchall()

                for row in resulset:
                    unaReserva = Reserva(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    reservas.append(unaReserva.toJSON())

            connection.close()
            return reservas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def getReserva(self, id_reserva):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM reserva WHERE id_reserva=%s", (id_reserva,))
                row = cursor.fetchone()

                unaReserva = None
                if row != None:
                    unaReserva = Reserva(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    unaReserva = unaReserva.toJSON()

            connection.close()
            return unaReserva
        except Exception as ex:
            raise Exception(ex)

    #Crear metodo que asigne el id de la solicitud parametro: el nombre de la solicitud
    @classmethod
    def getIdSolicitud(self, tipo):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_solicitud FROM solicitud WHERE tipo=%s", (tipo,))
                row = cursor.fetchone()

            connection.close()

            return row[0]
        except Exception as ex:
            raise Exception(ex)

    #Crear un metodo que asigne una mesa a una reserva parametro: numero_asistentes, fecha, hora
    @classmethod
    def asignarMesa(self, numero_asistentes, fecha, hora):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT numero_mesa FROM mesa WHERE capacidad>=%s", (numero_asistentes,))
                resulset = cursor.fetchall()

                #SELECT numero_mesa FROM mesa m INNER JOIN reserva r ON m.numero_mesa=r.numero_mesa WHERE m.capacidad>=%s AND r.fecha=%s AND r.hora!=%s

            with connection.cursor() as cursor:
                cursor.execute("SELECT numero_mesa FROM reserva WHERE fecha=%s AND hora=%s", (fecha, hora))
                resultados = cursor.fetchall()

            for row in resulset:
                if row not in resultados:
                    return row

            return None
        except Exception as ex:
            raise Exception(ex)



    #Mirar en el video el formateo de fechas SI SE NECESITA ESTADO: YA LO HICE FALTA PROBAR
    #Mirar como coloco el metodo retornarIDSolicitud en addReserva y updateReserva ESTADO: YA LO HICE FALTA PROBAR
    #Retornar mensaje de que no se pudo asignar mesa porque no tiene la capacidad disponible   CASO: cuando asignar mesa es None ESTADO: YA LO HICE FALTA PROBAR
    #Trigger del evento delete en la tabla mesa que cuando se borre un mesa se guarde su id en una tabla ESTADO: SON IDEAS OPCIONAL

    @classmethod
    def addReserva(self, reserva):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                if self.asignarMesa(reserva.numero_asistentes, reserva.fecha, reserva.hora) == None:
                    cursor.execute("INSERT INTO reserva VALUES (nextval('sec_reserva'), %s, %s, NULL, %s, %s, %s)",
                                   (reserva.cedula, self.getIdSolicitud(reserva.id_solicitud),
                                    reserva.numero_asistentes, reserva.fecha, reserva.hora))
                else:
                    cursor.execute("INSERT INTO reserva VALUES (nextval('sec_reserva'), %s, %s, %s, %s, %s, %s)", (reserva.cedula, self.getIdSolicitud(reserva.id_solicitud), self.asignarMesa(reserva.numero_asistentes, reserva.fecha, reserva.hora), reserva.numero_asistentes, reserva.fecha, reserva.hora))
                    affected_rows = cursor.rowcount
                    connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def deleteReserva(self, id_reserva):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM reserva WHERE id_reserva=%s", (id_reserva,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def updateReserva(self, reserva):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                if self.asignarMesa(reserva.numero_asistentes, reserva.fecha, reserva.hora) == None:
                    cursor.execute("UPDATE reserva SET cedula=%s, id_solicitud=%s, numero_mesa=NULL, "+
                                   "numero_asistentes=%s, fecha=%s, hora=%s WHERE id_reserva=%s",
                                   (reserva.cedula, self.getIdSolicitud(reserva.id_solicitud), reserva.numero_asistentes, reserva.fecha, reserva.hora, reserva.id_reserva))
                else:
                    cursor.execute("UPDATE reserva SET cedula=%s, id_solicitud=%s, numero_mesa=%s, " +
                                   "numero_asistentes=%s, fecha=%s, hora=%s WHERE id_reserva=%s",
                                   (reserva.cedula, self.getIdSolicitud(reserva.id_solicitud),
                                    self.asignarMesa(reserva.numero_asistentes, reserva.fecha, reserva.hora),
                                    reserva.numero_asistentes, reserva.fecha, reserva.hora, reserva.id_reserva))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
