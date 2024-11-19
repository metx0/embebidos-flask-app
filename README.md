# Aplicación Flask para el proyecto de Embebidos

## Cómo correr la aplicación

### Instalación de Python
Asegúrate de tener Python instalado en tu sistema. Para comprobarlo, puedes correr `python --version` en la terminal.

### Creación del ambiente virtual
Un ambiente virtual (virtual environment) sirve para aislar las dependencias que instales para el proyecto de aquellas instaladas globalmente, permitiendo usar las versiones que necesita el proyecto.

Para crearlo, ejecuta lo siguiente:
```
python -m venv .venv
```

Esto creará un directorio de nombre .venv, que será el ambiente virtual. 

### Instalación de dependencias
Ejecuta:
```
pip install -r requirements.txt
```
Esto instalará todas las dependencias listadas en el archivo requirements.txt

### Creación del archivo .env 
Para poder hacer la conexión con la base de datos MySQL necesitamos la contraseña. La contraseña la guardaremos como una variable de entorno.

Estando en el directorio raíz del proyecto, crea un archivo llamado `.env`. En él pondrás lo siguiente:
```
MYSQL_PASSWORD = tu_contraseña_del_usuario_root
```

Reemplaza el valor por la contraseña del usuario root de tu servidor MySQL local. 

Nota: asegúrate de que la base de datos se llame "db_its"

A este punto, el proyecto debería funcionar. 


## Cómo probar el proyecto

### Ejecuta la aplicación
Asegúrate de estar en el directorio raíz y ejecutar `python main.py`.

Esto pondrá en ejecución la aplicación Flask y la salida debería ser similar a lo siguiente:
```
* Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```

Ve a la dirección `http://127.0.0.1:5000` en tu navegador y debería aparecer `Bienvenido al servidor`.

###  Prueba los endpoints

En este punto, la API tiene unos cuantos endpoints que admiten peticiones GET, pero si quieres probar el endpoint que admite POST, necesitas una herramienta de testeo de APIs como Thunder Client (el cual puedes usar directamente en VS Code). 

El endpoint para hacer POST es `registrar-asistencia`, por lo que en Thunder Client deberás poner `http://127.0.0.1:5000/registrar-asistencia` en la URL a la que se hará la petición. 

En la petición POST tendrás que mandar un JSON con una clave "matrícula" que corresponda a la matrícula de algún estudiante de ITS. Para que la petición tenga éxito y cree un nuevo registro de asistencia la hora tendrá que ser válida. Puedes cambiar la hora en el archivo `api.py` que se encuentra en `app/`. En el diccionario `horario` cambia algún valor de la lista para que sea una hora válida, y si quieres igual la variable `minutos_tolerancia`. 

```python
horario = {"sistemas embebidos": ["19:00", "13:00"]}
```

### Ve los registros de asistencia

El endpoint que devuelve todos los registros de la tabla asistencias en un JSON es `/ver-registros`. 