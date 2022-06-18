# Rembe 📝

***Proyecto de Ingeniería de Software.***

***Semestre: 2022-2***

***Proyecto: Rembe***

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

### Pre-requisitos 📋

Para poner el sistema en funcionamiento es necesario:

- PostgreSQL: Tener las credenciales para una instalación en funcionamiento de la base de datos.
- Credenciales de Google: Tener los datos del ID de cliente y el token secreto para un proyecto de Google Cloud, con permisos para manipular los calendarios del usuario, de autenticación y de la URL sobre la que se va a desplegar el proyecto.

### Instalación 🔧

#### Docker

Para realizar la instalación con Docker es necesario tener esta herramienta instalada.

Localizado en el directorio raíz del proyecto, donde se encuentra el archivo `Dockerfile`, ejecutar el comando:

```
docker build --build-arg database_name=<database name> \
--build-arg database_user=<database user< \
--build-arg database_pass=<database password> \
--build-arg database_host=<database host> \
--build-arg database_port=<database port> \
--build-arg secret_key=<secret key> \
--build-arg google_client_id=<google client id> \
--build-arg google_secret=<google secret> \
-t <nombre repo>:latest .
```

sustituyendo los argumentos por sus valores adecuados. Posteriormente ejecutar:

```
docker run -dp 8000:8000 <nombre contenedor>
```

#### Manual

Para realizar la instalación manual es necesario definir las variables de ambiente:

- SECRET_KEY
- DATABASE_NAME
- DATABASE_USER
- DATABASE_PASS
- DATABASE_HOST
- DATABASE_PORT
- GOOGLE_CLIENT_ID
- GOOGLE_SECRET

Recomendamos definirlas en el archivo `rembe/settings/.env` para ser detectadas automáticamente por el proyecto.

Para instalar las dependencias ejecutar el comando `pip install -r requirements.txt` en la raíz del proyecto. Recomendamos utilizar un ambiente virtual para mantener contenida la instalación de Python con las bibliotecas del proyecto.

Posteriormente, ejecutar el proyecto con el comando `./manage.py runserver` en la raíz del proyecto.

Igualmente es posible adecuar esto mismo para que funcione con un servidor HTTP como Apache o Nginx.

## Despliegue 📦

- GitHub Actions
- Docker
- Azure Web Apps

## Construido con 🛠️

- Python
- Django
- PostgreSQL

## Notas 📝

## Autores ✒️

- **David Hernández Uriostegui** - [DavidHdezU](https://github.com/DavidHdezU)
- **Francisco EmmanuelDel Moral Morales** - [cocisran](https://github.com/cocisran)
- **Juan Pablo Yamamoto Zazueta** - [JPYamamoto](https://github.com/JPYamamoto)
- **Julio Vázquez Alvarez** - [JulsVazquez](https://github.com/JulsVazquez)

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita un café ☕ a alguien del equipo.



---
⌨️ con ❤️ por [Rembe](https://github.com/JPYamamoto/rembe) 😊
