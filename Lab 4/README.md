
# **Laboratio 4 Tópicos Especiales de Telemática.**


RabbitMQ: Simulación de un gestor de tareas para procesamiento distribuido

## **Requerimientos**

**Python version**

3.7.10

**pip version**

20.2.2

## **Configuracion inicial**

Es necesario instalar la libreria pika
```bash
$ pip install pika
```
## **Ejecución**


### **Correr Servidor**

Por defecto:
``` bash
$ python3 Server/server.py
```

La dirección IP por defecto corresponde a la instancia con RabbitMQ desplegada en Ec2, para definir la IP manualmente:

``` bash
$ python3 Server/server.py -i {ip_address}
```

Para obtener ayuda sobre la implementación:

``` bash
$ python3 Server/server.py -h
```

### **Correr Cliente**

Por defecto:
``` bash
$ python3 Client/client.py
```

La dirección IP por defecto corresponde a la instancia con RabbitMQ desplegada en Ec2, para definir la IP manualmente:

``` bash
$ python3 Client/client.py -i {ip_address}
```

Para obtener ayuda sobre la implementación:

``` bash
$ python3 Client/client.py -h
```


## **Aclaraciones**

- Pueden desplegarse tantos clientes como servidores se desee

- Para enviar un mensaje es necesario correr el cliente y diligenciar la informacion correspondiente

- No es necesario desplegar el servidor de forma previa, ya que todo el proceso se hace de forma asíncrona

- Una vez desplegado el servidor(es), éste se encargará de enviar notificaciones al usuario por correo de la tarea realizada.


## **Protocolo AMQP**

![alt text](https://github.com/agarciam14/ST0263-TE_Telematica/blob/master/Lab%204/mind-map.jpg)