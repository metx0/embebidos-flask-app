from flask import Blueprint, request
from datetime import datetime, timedelta
from crud import insertar_registro, recuperar_registros

api = Blueprint("api", __name__)

horario = {"concurrencia": "11:00", "sistema embebidos": "13:00"}

minutos_tolerancia = 15


@api.route("registrar-asistencia", methods=["POST"])
def registrar_asistencia():
    """
    Registra la asistencia de un estudiante según su matrícula y
    valida la hora de registro
    """

    data = request.get_json()
    matricula = data.get("matricula")

    # El cliente no envió una petición correcta
    if not matricula:
        # Devuelve un código 400 y un mensaje de error en un JSON
        return ({"error": "La matrícula es obligatoria"}, 400)

    hora_actual = datetime.now().time().replace(second=0, microsecond=0)

    """ 
    La hora es válida si es mayor o igual a la hora de entrada 
    y menor o igual a la hora limite
    """

    hora_valida = False
    # La materia a la que está ingresando el alumno
    materia_asistencia = ""

    for materia, hora_entrada in horario.items():
        hora_entrada_obj = datetime.strptime(hora_entrada, "%H:%M").time()

        # Por ejemplo, para Concurrencia la hora límite sería 11:15
        hora_limite = (
            datetime.combine(datetime.today(), hora_entrada_obj)
            + timedelta(minutes=minutos_tolerancia)
        ).time()

        if hora_actual >= hora_entrada_obj and hora_actual <= hora_limite:
            hora_valida = True
            materia_asistencia = materia
            print("La hora actual está dentro del rango permitido")
            break

    if hora_valida:
        # Escribir el registro en la BD
        # insertar_registro(matricula, materia_asistencia, hora_actual.strftime("%H:%M"))        

        # Regresar un JSON que indique que la asistencia ha sido registrada
        return (
            {
                "mensaje": f"Asistencia registrada para la matrícula {matricula} a la materia {materia_asistencia}",
                "hora": hora_actual.strftime("%H:%M"),
            },
            201,
        )
    else:
        # Indicar que la hora ya no es válida
        return (
            {
                "error": f"La hora de ingreso no es válida para la matrícula {matricula}",
                "hora": hora_actual.strftime("%H:%M"),
            },
            400,
        )


@api.route("ver-registros", methods=["GET"])
def mostrar_registros():
    """
    Devuelve todos los registros de la tabla 'asistencias' en un JSON
    """
