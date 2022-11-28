from flask import Blueprint, jsonify, request, render_template
from Models.ClienteModel import ClienteModel
from Models.Entities.Cliente import Cliente

main = Blueprint('cliente_blueprint', __name__)

@main.route("/listado", methods = ['GET'])
def getClientes():
    try:
        clientes = ClienteModel.getClientes()
        #return jsonify(clientes)
        return render_template('listado.html', clientes = clientes)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route("/ver/<string:cedula>", methods = ['GET'])
def getCliente(cedula):
    try:
        cliente = ClienteModel.getCliente(cedula)
        if cliente!=None:
            #return jsonify(cliente)
            return render_template('listado.html', cliente = cliente)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route("/add", methods = ['POST'])
def addCliente():
    try:
        cedula = request.json['cedula']
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        correo = request.json['correo']
        telefono = request.json['telefono']

        cliente = Cliente(cedula, nombre, apellido, correo, telefono)

        affected_rows = ClienteModel.addCliente(cliente)

        if affected_rows == 1:
            return jsonify(cliente.cedula)
        else:
            return jsonify({'message': "Error en la inserción"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route("/delete/<string:cedula>", methods = ['DELETE'])
def deleteCliente(cedula):
    try:
        affected_rows = ClienteModel.deleteCliente(cedula)

        if affected_rows == 1:
            return jsonify(cedula)
        else:
            return jsonify({'message': "No se pudo eliminar el cliente"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route("/update/<string:cedula>", methods = ['PUT'])
def updateCliente(cedula):
    try:
        correo = request.json['correo']
        telefono = request.json['telefono']

        cliente = Cliente(cedula, None, None, correo, telefono)

        affected_rows = ClienteModel.updateCliente(cliente)

        if affected_rows == 1:
            return jsonify(cliente.cedula)
        else:
            return jsonify({'message': "No se pudo actualizar el cliente"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
