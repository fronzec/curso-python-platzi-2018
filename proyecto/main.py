clients = 'pablo,ricardo,'


def create_client(client_name):
    # Permite usar una variable global dentro de la funcion
    global clients
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print("El cliente ya esta en la lista de clientes")


def list_clients():
    global clients
    print(clients)


def update_client(current_client_name, updated_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(current_client_name, updated_client_name)
    else:
        _print_client_not_found()


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        _print_client_not_found()


def search_client(client_name):
    global clients
    clients_list = clients.split(',')
    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True


def _print_client_not_found():
    print("Client not found on client list")


def _add_comma():
    global clients
    clients += ','


def _print_welcome():
    print('Bienvenidos a la app de ventas')
    print('*' * 50)
    print('¿Que quisieras hacer hoy?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print('')


def _get_client_name():
    return input("¿Cual es el nombre del cliente? ")


if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        new_client_name = input("What is the updated client name?")
        update_client(client_name, new_client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in the client\'s  list')
        else:
            print('The client {} is not in client\'s list'.format(client_name))
    else:
        print("Invalid command")
