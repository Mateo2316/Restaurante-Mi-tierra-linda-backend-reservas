from Database.db import getConnection
from .Entities.Mesa import Mesa

class MesaModel():

    @classmethod
    def getMesas(self):
        try:
            connection = getConnection()
            mesas = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM mesa")
                resulset = cursor.fetchall()

                for row in resulset:
                    unaMesa = Mesa(row[0], row[1])
                    mesas.append(unaMesa.toJSON())

            connection.close()
            return mesas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def getMesa(self, numero_mesa):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM mesa WHERE numero_mesa=%s", (numero_mesa,))
                row = cursor.fetchone()

                unaMesa = None
                if row != None:
                    unaMesa = Mesa(row[0], row[1])
                    unaMesa = unaMesa.toJSON()

            connection.close()
            return unaMesa
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def addMesa(self, mesa):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO mesa VALUES (nextval('sec_num_mesa'), %s)", (mesa.capacidad,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def deleteMesa(self, numero_mesa):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM mesa WHERE numero_mesa=%s", (numero_mesa,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    # solo actulizo la capacidad, consultar eso con los compañeros
    @classmethod
    def updateMesa(self, mesa):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("UPDATE mesa SET capacidad=%s WHERE numero_mesa=%s", (mesa.capacidad, mesa.numero_mesa))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
