from flask import Blueprint, request, render_template
from .crud import recuperar_registros

vistas = Blueprint("vistas", __name__)

# La plantilla se renderiza en la ruta raíz 
@vistas.route('/')
def mostrar_asistencias():
    """
    Renderiza un HTML que muestra una tabla con 
    las asistencias de los alumnos a las materias
    """

    registros = recuperar_registros()
    return render_template('tabla.html', asistencias=registros)
