from flask import Blueprint, request
from datetime import datetime

api = Blueprint("api", __name__)

horario = {"concurrencia": 11, "sistema embebidos": 13}

minutos_tolerancia = 15


@api.route("registrar-asistencia", methods=["POST"])
def registrar_asistencia():
    data = request.get_json()
    matricula = data.get("matricula")

    # El cliente no envió una petición correcta
    if not matricula:
        # Devuelve un código 400 y un mensaje de error en un JSON
        return ({"error": "La matrícula es obligatoria"}, 400)

    # Validar la hora de registro

    hora_actual = datetime.now().strftime("%H:%M")

    respuesta_json = {"matricula": matricula, "hora": hora_actual}

    return (respuesta_json, 200)

    # Escribir el registro en la BD
