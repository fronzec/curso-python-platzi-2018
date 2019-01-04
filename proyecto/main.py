clientes = 'pablo,ricardo,'


def create_client(client_name):
    # Permite usar una variable global dentro de la funcion
    global clientes
    if client_name not in clientes:
        clientes += client_name
        _add_comma()
    else:
        print("El cliente ya esta en la lista de clientes")


def list_clients():
    global clientes
    print(clientes)


def _add_comma():
    global clientes
    clientes += ','


def _print_welcome():
    print('Bienvenidos a la app de ventas')
    print('*' * 50)
    print('¿Que quisieras hacer hoy?')
    print('[C]reate client')
    print('[D]elete client')
    print('')


if __name__ == '__main__':
    _print_welcome()
    command = input()
    if command == 'C':
        client_name = input("¿Cual es el nombre del cliente? ")
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    else:
        print("Invalid command")
