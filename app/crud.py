from mysql import connector
from dotenv import load_dotenv
import os
from os.path import join, dirname

""" 
Métodos para interactuar con la base de datos MySQL que contiene los registros 
de las asistencias
Proporciona los métodos de inserción y lectura de la tabla 
"""

# TODO: cambiar las queries por las que se usarán en el esquema real


def recuperar_contrasena_mysql() -> str:
    # El archivo .env se encuentra en el directorio raíz
    dotenv_path = join(dirname(dirname(__file__)), ".env")
    load_dotenv(dotenv_path)
    mysql_contrasena = os.getenv("MYSQL_PASSWORD")
    return mysql_contrasena


def insertar_registro(id, descripcion, semestre, creditos) -> None:
    query = "INSERT INTO materias VALUES (%s, %s, %s, %s)"
    valores = (id, descripcion, semestre, creditos)
    contrasena = recuperar_contrasena_mysql()

    try:
        with connector.connect(
            host="localhost", user="root", password=contrasena, database="db_escuela"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, valores)
                connection.commit()

                registros = cursor.fetchall()

                for fila in registros:
                    print(fila)
    except connector.Error as e:
        print(e)


def recuperar_registros() -> list:
    contrasena = recuperar_contrasena_mysql()

    try:
        with connector.connect(
            host="localhost", user="root", password=contrasena, database="db_escuela"
        ) as connection:
            with connection.cursor() as cursor:
                query = "SELECT * FROM materias"
                cursor.execute(query)

                registros = cursor.fetchall()

                for fila in registros:
                    print(fila)

                return registros
    except connector.Error as e:
        print(e)


if __name__ == "__main__":
    recuperar_registros()
    # insertar_registro(124, "Programación web", 6, 4)
