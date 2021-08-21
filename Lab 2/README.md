# ST0263-TE_Telematica 

# Autor: Anthony García Moncada

## **Documentación Laboratio 2 Tópicos Especiales de Telemática.**

## Chat con comunicacion por protocolo HTTP

**Protocolo y Arquitectura**

En este laboratorio se realizo una comunicacion por Protocolo HTTP
tambien se realizo en una arquitectura Cliente/Servidor, con el agregado de un client server para recibir los mensajes enviados por el servidor central, aún así se conserva la arquitectura, ya que toda la comunicación es intermediada por el servidor.

## **Requerimientos**

**Python version**

3.7.10

**pip version**

pip 20.2.2

**Configuracion inicial**

- No es necesario instalar ninguna libreria extra para ejecutar el proyecto

- Se debe cambiar en el archivo **client.py** la dirección del servidor (la dispuesta corresponde a la dirección ip elástica de la instancia desplegada en AWS), en el caso local por "127.0.0.1" y en el caso de una instancia en AWS se debe colocar la dirección elástica de la misma o su ip pública en su defecto.


- **Correr Servidor**
$ python3 Server/server.py

- **Correr Cliente**
$python3 Client/client.py

**Aclaraciones**

- Pueden conectarse tantos clientes como se desee, pero el servidor siempre desbe estar activo de forma previa para el correcto funcionamiento

- El archivo **clientServer.py** se encarga de arrancar el servicio del cliente encargado de recibir los mensajes enviados por los demás clientes a través del servidor

- Al conectar un cliente, este te va a pedir digitar un nombre, una vez digitado, podrás ver cuantas clientes hay en línea además del conectado

- Cuando un cliente se conecta, los demás clientes en línea recibirán un mensaje avisándoles que este se ha conectado, lo mismo aplica al desconectarse

- Para desconectarse de forma efectiva, los clientes deben enviar el mensaje **'salir'**, de este modo será removido del grupo de direcciones disponibles y terminará el programa