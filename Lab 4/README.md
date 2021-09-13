# ST0263-TE_Telematica 

# Autor: Anthony García Moncada

## **Documentación Laboratio 4 Tópicos Especiales de Telemática.**

## RabbitMQ

Simulación de un gestor de tareas para procesamiento distribuido

## **Requerimientos**

**Python version**

3.7.10

**pip version**

pip 20.2.2

**Configuracion inicial**

- Es necesario instalar la libreria pika
$ pip install pika

- Se debe cambiar en los archivos **client.py** y **server.py** la dirección del servidor con RabbitMQ (la dispuesta corresponde a la dirección ip elástica de la instancia desplegada en AWS).


- **Correr Servidor**
$ python3 Server/server.py

- **Correr Cliente**
$python3 Client/client.py

**Aclaraciones**

- Pueden desplegarse tantos clientes como servidores se desee

- Para enviar un mensaje es necesario correr el cliente y diligenciar la informacion correspondiente

- No es necesario desplegar el servidor de forma previa, ya que todo el proceso se hace de forma asíncrona


## **Protocolo AMQP**

![alt text](http://github.com/agarciam14/ST0263-TE_Telematica/tree/master/Lab 4/mind-map.jpg)