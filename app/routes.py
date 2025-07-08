from flask import Blueprint, jsonify, request
from .models import Credito
from . import db

routes = Blueprint('routes', __name__)

@routes.route('/creditos', methods=['GET'])
def obtener_creditos():
    creditos = Credito.query.all()

    resultado = []
    for c in creditos:
        resultado.append({
            'id': c.id,
            'cliente': c.cliente,
            'monto': c.monto,
            'tasa_interes': c.tasa_interes,
            'plazo': c.plazo,
            'fecha_otorgamiento': c.fecha_otorgamiento
        })
	
    return jsonify(resultado)

@routes.route('/creditos', methods=['POST'])
def crear_credito():
    data = request.get_json()

    # Validar campos obligatorios
    campos_requeridos = ['cliente', 'monto', 'tasa_interes', 'plazo', 'fecha_otorgamiento']
    for campo in campos_requeridos:
        if campo not in data:
            return jsonify({'error': f'Campo faltante: {campo}'}), 400

    try:
        nuevo_credito = Credito(
            cliente=data['cliente'],
            monto=float(data['monto']),
            tasa_interes=float(data['tasa_interes']),
            plazo=int(data['plazo']),
            fecha_otorgamiento=data['fecha_otorgamiento']
        )

        db.session.add(nuevo_credito)
        db.session.commit()

        return jsonify({'mensaje': 'Crédito creado correctamente'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@routes.route('/creditos/<int:id>', methods=['PUT'])
def actualizar_credito(id):
    credito = Credito.query.get(id)

    if not credito:
        return jsonify({'error': 'Crédito no encontrado'}), 404

    data = request.get_json()

    # Validar campos obligatorios
    campos_requeridos = ['cliente', 'monto', 'tasa_interes', 'plazo', 'fecha_otorgamiento']
    for campo in campos_requeridos:
        if campo not in data:
            return jsonify({'error': f'Campo faltante: {campo}'}), 400

    try:
        # Actualizar campos del crédito existente
        credito.cliente = data['cliente']
        credito.monto = float(data['monto'])
        credito.tasa_interes = float(data['tasa_interes'])
        credito.plazo = int(data['plazo'])
        credito.fecha_otorgamiento = data['fecha_otorgamiento']

        db.session.commit()

        return jsonify({'mensaje': f'Crédito con id {id} actualizado correctamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@routes.route('/creditos/<int:id>', methods=['DELETE'])
def eliminar_credito(id):
    credito = Credito.query.get(id)

    if not credito:
        return jsonify({'error': 'Crédito no encontrado'}), 404

    db.session.delete(credito)
    db.session.commit()

    return jsonify({'mensaje': f'Crédito con id {id} eliminado'}), 200

