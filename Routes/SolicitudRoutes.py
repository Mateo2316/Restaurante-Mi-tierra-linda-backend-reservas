from flask import Blueprint, jsonify, request
from Models.SolicitudModel import SolicitudModel
from Models.Entities.Solicitud import Solicitud

main = Blueprint('solicitud_blueprint', __name__)

@main.route("/listado", methods = ['GET'])
def getSolicitudes():
    try:
        solicitudes = SolicitudModel.getSolicitudes()
        return jsonify(solicitudes)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route("/ver/<int:id>", methods = ['GET'])
def getSolicitud(id):
    try:
        solicitud = SolicitudModel.getSolicitud(id)
        if solicitud!=None:
            return jsonify(solicitud)
        else:
            return jsonify({}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route("/add", methods = ['POST'])
def addSolicitud():
    try:
        tipo = request.json['tipo']
        descripcion = request.json['descripcion']
        valor = request.json['valor']

        solicitud = Solicitud(None, tipo, descripcion, valor)

        affected_rows = SolicitudModel.addSolicitud(solicitud)

        if affected_rows == 1:
            return jsonify(solicitud.id)
        else:
            return jsonify({'message': "Error en la inserción"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route("/delete/<int:id>", methods = ['DELETE'])
def deleteCliente(id):
    try:
        affected_rows = SolicitudModel.deleteSolicitud(id)

        if affected_rows == 1:
            return jsonify(id)
        else:
            return jsonify({'message': "No se pudo eliminar la solicitud"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route("/update/<int:id>", methods = ['PUT'])
def updateCliente(id):
    try:
        tipo = request.json['tipo']
        descripcion = request.json['descripcion']
        valor = request.json['valor']

        solicitud = Solicitud(id, tipo, descripcion, valor)

        affected_rows = SolicitudModel.updateSolicitud(solicitud)

        if affected_rows == 1:
            return jsonify(solicitud.id)
        else:
            return jsonify({'message': "No se pudo actualizar la solicitud"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
