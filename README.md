# Rembe 馃摑

***Proyecto de Ingenier铆a de Software.***

***Semestre: 2022-2***

***Proyecto: Rembe***

## Comenzando 馃殌

_Estas instrucciones te permitir谩n obtener una copia del proyecto en funcionamiento en tu m谩quina local para prop贸sitos de desarrollo y pruebas._

### Pre-requisitos 馃搵

Para poner el sistema en funcionamiento es necesario:

- PostgreSQL: Tener las credenciales para una instalaci贸n en funcionamiento de la base de datos.
- Credenciales de Google: Tener los datos del ID de cliente y el token secreto para un proyecto de Google Cloud, con permisos para manipular los calendarios del usuario, de autenticaci贸n y de la URL sobre la que se va a desplegar el proyecto.

### Instalaci贸n 馃敡

#### Docker

Para realizar la instalaci贸n con Docker es necesario tener esta herramienta instalada.

Localizado en el directorio ra铆z del proyecto, donde se encuentra el archivo `Dockerfile`, ejecutar el comando:

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

Para realizar la instalaci贸n manual es necesario definir las variables de ambiente:

- SECRET_KEY
- DATABASE_NAME
- DATABASE_USER
- DATABASE_PASS
- DATABASE_HOST
- DATABASE_PORT
- GOOGLE_CLIENT_ID
- GOOGLE_SECRET

Recomendamos definirlas en el archivo `rembe/settings/.env` para ser detectadas autom谩ticamente por el proyecto.

Para instalar las dependencias ejecutar el comando `pip install -r requirements.txt` en la ra铆z del proyecto. Recomendamos utilizar un ambiente virtual para mantener contenida la instalaci贸n de Python con las bibliotecas del proyecto.

Posteriormente, ejecutar el proyecto con el comando `./manage.py runserver` en la ra铆z del proyecto.

Igualmente es posible adecuar esto mismo para que funcione con un servidor HTTP como Apache o Nginx.

## Despliegue 馃摝

- GitHub Actions
- Docker
- Azure Web Apps

## Construido con 馃洜锔?

- Python
- Django
- PostgreSQL

## Notas 馃摑

## Autores 鉁掞笍

- **David Hern谩ndez Uriostegui** - [DavidHdezU](https://github.com/DavidHdezU)
- **Francisco EmmanuelDel Moral Morales** - [cocisran](https://github.com/cocisran)
- **Juan Pablo Yamamoto Zazueta** - [JPYamamoto](https://github.com/JPYamamoto)
- **Julio V谩zquez Alvarez** - [JulsVazquez](https://github.com/JulsVazquez)

## Expresiones de Gratitud 馃巵

* Comenta a otros sobre este proyecto 馃摙
* Invita un caf茅 鈽? a alguien del equipo.



---
鈱笍 con 鉂わ笍 por [Rembe](https://github.com/JPYamamoto/rembe) 馃槉
