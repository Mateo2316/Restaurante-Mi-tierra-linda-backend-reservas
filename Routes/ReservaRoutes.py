from flask import Blueprint, jsonify, request
from Models.ReservaModel import ReservaModel
from Models.Entities.Reserva import Reserva

main = Blueprint('reserva_blueprint', __name__)

@main.route("/listado", methods = ['GET'])
def getReservas():
    try:
        reservas = ReservaModel.getReservas()
        return jsonify(reservas)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route("/ver/<int:id_reserva>", methods = ['GET'])
def getReserva(id_reserva):
    try:
        reserva = ReservaModel.getReserva(id_reserva)
        if reserva!=None:
            return jsonify(reserva)
        else:
            return jsonify({}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route("/add", methods = ['POST'])
def addReserva():
    try:
        cedula = request.json['cedula']
        id_solicitud = request.json['id_solicitud']
        numero_asistentes = request.json['numero_asistentes']
        fecha = request.json['fecha']
        hora = request.json['hora']

        reserva = Reserva(None, cedula, id_solicitud, None, numero_asistentes, fecha, hora)

        affected_rows = ReservaModel.addReserva(reserva)

        if affected_rows == 1:
            return jsonify({'message': "Exito"})
        else:
            return jsonify({'message': "Error en la inserción"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route("/delete/<int:id_reserva>", methods = ['DELETE'])
def deleteReserva(id_reserva):
    try:
        affected_rows = ReservaModel.deleteReserva(id_reserva)

        if affected_rows == 1:
            return jsonify(id_reserva)
        else:
            return jsonify({'message': "No se pudo eliminar la reserva"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route("/update/<int:id_reserva>", methods = ['PUT'])
def updateReserva(id_reserva):
    try:
        cedula = request.json['cedula']
        id_solicitud = request.json['id_solicitud']
        numero_asistentes = request.json['numero_asistentes']
        fecha = request.json['fecha']
        hora = request.json['hora']

        reserva = Reserva(id_reserva, cedula, id_solicitud, None, numero_asistentes, fecha, hora)

        affected_rows = ReservaModel.updateReserva(reserva)

        if affected_rows == 1:
            return jsonify(reserva.id_reserva)
        else:
            return jsonify({'message': "No se pudo actualizar la reserva"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
