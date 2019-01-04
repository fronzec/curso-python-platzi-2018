clientes = 'pablo,ricardo,'


def create_client(client_name):
    # Permite usar una variable global dentro de la funcion
    global clientes
    clientes += client_name
    _add_comma()


def list_clients():
    global clientes
    print(clientes)


def _add_comma():
    global clientes
    clientes += ','


if __name__ == '__main__':
    list_clients()
    create_client('david')
    print(clientes)
