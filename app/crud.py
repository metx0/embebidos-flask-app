from mysql import connector
from dotenv import load_dotenv
import os
from os.path import join, dirname

""" 
Métodos para interactuar con la base de datos MySQL que contiene los registros 
de las asistencias
Proporciona los métodos de inserción y lectura de la tabla 
"""


def recuperar_contrasena_mysql() -> str:
    # El archivo .env se encuentra en el directorio raíz
    dotenv_path = join(dirname(dirname(__file__)), ".env")
    load_dotenv(dotenv_path)
    mysql_contrasena = os.getenv("MYSQL_PASSWORD")
    return mysql_contrasena


# La tabla Asistencias necesita la matrícula, la materia, y la fecha (timestamp)
def insertar_registro(matricula: int, materia: str, fecha) -> None:
    query = "INSERT INTO asistencias (matricula, materia, fecha) VALUES (%s, %s, %s)"
    valores = (matricula, materia, fecha)
    contrasena = recuperar_contrasena_mysql()

    try:
        with connector.connect(
            host="localhost", user="root", password=contrasena, database="db_its"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, valores)
                connection.commit()
    except connector.Error as e:
        print(e)


def recuperar_registros() -> list:
    contrasena = recuperar_contrasena_mysql()

    try:
        with connector.connect(
            host="localhost", user="root", password=contrasena, database="db_its"
        ) as connection:
            with connection.cursor() as cursor:
                # Necesitamos saber el nombre del alumno al que corresponde la matrícula
                query = """
                    SELECT id_asistencia, 
                        a.matricula, 
                        materia, 
                        fecha, 
                        CONCAT(al.nombre, ' ', al.apellido) AS nombre_completo 
                    FROM asistencias a
                    JOIN alumnos al ON a.matricula = al.matricula 
                    """
                
                cursor.execute(query)

                # Los nombres de las columnas de la tabla
                columnas = [desc[0] for desc in cursor.description]
                registros = cursor.fetchall()

                # Crear una lista de diccionarios que representa a todos los registros
                resultado = []

                for fila in registros:
                    dicc = {}

                    for indice, nombre_columna in enumerate(columnas):
                        # MySQL nos devuelve la fecha como un objeto datetime, así que tenemos que pasarlo a string
                        if nombre_columna == "fecha":
                            fecha_obj = fila[indice]
                            dicc[nombre_columna] = fecha_obj.strftime(
                                "%H:%M %d-%m-%Y"
                            )
                        else:
                            dicc[nombre_columna] = fila[indice]

                    resultado.append(dicc)

                return resultado
    except connector.Error as e:
        print(e)


if __name__ == "__main__":
    registros = recuperar_registros()
    for registro in registros:
        print(registro)

    # insertar_registro(70690, "sistemas embebidos", "2024-11-16 14:30:00")
