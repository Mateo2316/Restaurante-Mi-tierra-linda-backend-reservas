from Database.db import getConnection
from .Entities.Cliente import Cliente

class ClienteModel():

    @classmethod
    def getClientes(self):
        try:
            connection = getConnection()
            clientes = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM cliente ORDER BY apellido ASC")
                resulset = cursor.fetchall()

                for row in resulset:
                    unCliente = Cliente(row[0], row[1], row[2], row[3], row[4])
                    clientes.append(unCliente.toJSON())

            connection.close()
            return clientes
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def getCliente(self, cedula):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM cliente WHERE cedula=%s", (cedula,))
                row = cursor.fetchone()

                unCliente = None
                if row != None:
                    unCliente = Cliente(row[0], row[1], row[2], row[3], row[4])
                    unCliente = unCliente.toJSON()

            connection.close()
            return unCliente
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def addCliente(self, cliente):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO cliente VALUES (%s, %s, %s, %s, %s)", (cliente.cedula, cliente.nombre, cliente.apellido, cliente.correo, cliente.telefono))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def deleteCliente(self, cedula):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM cliente WHERE cedula=%s", (cedula,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def updateCliente(self, cliente):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("UPDATE cliente SET correo=%s, telefono=%s WHERE cedula=%s", (cliente.correo, cliente.telefono, cliente.cedula))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
