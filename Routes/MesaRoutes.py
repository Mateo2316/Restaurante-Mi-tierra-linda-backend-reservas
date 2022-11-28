from flask import Blueprint, jsonify, request
from Models.MesaModel import MesaModel
from Models.Entities.Mesa import Mesa

main = Blueprint('mesa_blueprint', __name__)

@main.route("/listado", methods = ['GET'])
def getMesas():
    try:
        mesas = MesaModel.getMesas()
        return jsonify(mesas)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route("/ver/<int:numero_mesa>", methods = ['GET'])
def getMesa(numero_mesa):
    try:
        mesa = MesaModel.getMesa(numero_mesa)
        if mesa!=None:
            return jsonify(mesa)
        else:
            return jsonify({}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route("/add", methods = ['POST'])
def addMesa():
    try:
        capacidad = request.json['capacidad']

        mesa = Mesa(None, capacidad)

        affected_rows = MesaModel.addMesa(mesa)

        if affected_rows == 1:
            return jsonify(mesa.numero_mesa)
        else:
            return jsonify({'message': "Error en la inserción"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route("/delete/<int:numero_mesa>", methods = ['DELETE'])
def deleteMesa(numero_mesa):
    try:
        affected_rows = MesaModel.deleteMesa(numero_mesa)

        if affected_rows == 1:
            return jsonify(numero_mesa)
        else:
            return jsonify({'message': "No se pudo eliminar la mesa"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route("/update/<int:numero_mesa>", methods = ['PUT'])
def updateMesa(numero_mesa):
    try:
        capacidad = request.json['capacidad']

        mesa = Mesa(numero_mesa, capacidad)

        affected_rows = MesaModel.updateMesa(mesa)

        if affected_rows == 1:
            return jsonify(mesa.numero_mesa)
        else:
            return jsonify({'message': "No se pudo actualizar la disponibilidad de la mesa"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
