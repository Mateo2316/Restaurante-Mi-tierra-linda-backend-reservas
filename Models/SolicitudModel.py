from Database.db import getConnection
from .Entities.Solicitud import Solicitud

class SolicitudModel():

    @classmethod
    def getSolicitudes(self):
        try:
            connection = getConnection()
            solicitudes = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM solicitud")
                resulset = cursor.fetchall()

                for row in resulset:
                    unaSolicitud = Solicitud(row[0], row[1], row[2], row[3])
                    solicitudes.append(unaSolicitud.toJSON())

            connection.close()
            return solicitudes
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def getSolicitud(self, id):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM solicitud WHERE id_solicitud=%s", (id,))
                row = cursor.fetchone()

                unaSolicitud = None
                if row != None:
                    unaSolicitud = Solicitud(row[0], row[1], row[2], row[3])
                    unaSolicitud = unaSolicitud.toJSON()

            connection.close()
            return unaSolicitud
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def addSolicitud(self, solicitud):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO solicitud VALUES (nextval('sec_solicitud'), %s, %s, %s)", (solicitud.tipo, solicitud.descripcion, solicitud.valor))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def deleteSolicitud(self, id):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM solicitud WHERE id_solicitud=%s", (id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def updateSolicitud(self, solicitud):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("UPDATE solicitud SET tipo=%s, descripcion=%s, valor=%s WHERE id_solicitud=%s", (solicitud.tipo, solicitud.descripcion, solicitud.valor, solicitud.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
