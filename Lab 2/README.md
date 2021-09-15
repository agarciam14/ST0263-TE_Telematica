# **Laboratio 2 Tópicos Especiales de Telemática.**

Chat con comunicacion por protocolo HTTP

**Protocolo y Arquitectura**

En este laboratorio se realizó una comunicación por Protocolo HTTP, también se realizó en una arquitectura Cliente/Servidor, con el agregado de un client server para recibir los mensajes enviados por el servidor central, aún así se conserva la arquitectura, ya que toda la comunicación es intermediada por el servidor.

## **Requerimientos**

**Python version**

3.7.10

**pip version**

20.2.2

## **Configuracion inicial**

No es necesario instalar ninguna libreria extra para ejecutar el proyecto
## **Ejecución**


### **Correr Servidor**
``` bash
$ python3 Server/server.py
```

### **Correr Cliente**

Por defecto:
``` bash
$ python3 Client/client.py
```

La dirección IP por defecto corresponde a la instancia desplegada en Ec2, para definir la IP manualmente, o el puerto:

``` bash
$ python3 Client/client.py [-i {ip_address}] [-p {port}]
```

Para obtener ayuda sobre la implementación:

``` bash
$ python3 Client/client.py -h
```

**Aclaraciones**

- Pueden conectarse tantos clientes como se desee, pero el servidor siempre desbe estar activo de forma previa para el correcto funcionamiento

- El archivo **clientServer.py** se encarga de arrancar el servicio del cliente encargado de recibir los mensajes enviados por los demás clientes a través del servidor

- Al conectar un cliente, este te va a pedir digitar un nombre, una vez digitado, podrás ver cuantas clientes hay en línea además del conectado

- Cuando un cliente se conecta, los demás clientes en línea recibirán un mensaje avisándoles que este se ha conectado, lo mismo aplica al desconectarse

- Para desconectarse de forma efectiva, los clientes deben enviar el mensaje **'salir'**, de este modo será removido del grupo de direcciones disponibles y terminará el programa