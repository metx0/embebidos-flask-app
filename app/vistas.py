from flask import Blueprint, request

vistas = Blueprint("vistas", __name__)

""" 
Los datos se deben devolver como un arreglo de diccionarios, en los que 
cada elemento es un registro de la tabla, con las claves de nombre, matrícula, materia,
hora de ingreso, etc. 
"""

datos_prueba = [
    {
        
    }
]


@vistas.route('/ver-asistencias')
def mostrar_asistencias():
    """
    Renderiza un HTML que muestra las tablas de materias
    y las asistencias de los alumnos
    """