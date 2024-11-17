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

A este punto, el proyecto debería funcionar. 


## Cómo probar el proyecto
Asegúrate de estar en el directorio raíz y ejecutar `python main.py`.

Esto pondrá en ejecución la aplicación Flask y la salida debería ser similar a lo siguiente:
```
* Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```

Ve a la dirección `http://127.0.0.1:5000` en tu navegador y debería aparecer `Bienvenido al servidor`.

En este punto, la API tiene unos cuantos endpoints que admiten peticiones GET, pero si quieres probar el endpoint que admite POST, necesitas una herramienta de testeo de APIs como Thunder Client (el cual puedes usar directamente en VS Code). 

El endpoint para hacer POST es `registrar-asistencia`, por lo que en Thunder Client deberás poner `http://127.0.0.1:5000/registrar-asistencia` en la URL a la que se hará la petición. 