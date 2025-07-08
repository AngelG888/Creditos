from flask import Blueprint, jsonify
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