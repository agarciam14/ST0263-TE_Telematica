def msg_to_all(clients, msg, cliente):
    for c in clients:
        try:
            if c != cliente:
                c.send(msg)
        except:
            clientes.remove(c)