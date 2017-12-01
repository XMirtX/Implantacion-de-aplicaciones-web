def add_contact(phone_book, name, phone):
    if name in phone_book:
        print("El contacto existe")
    else:
        phone_book[name] = phone
    print("Contacto guardado con exito")


def del_contact(phone_book, name):
    if name in phone_book:
        del(phone_book[name])


def list_contact(phone_book):
    for name, phone in phone_book.items():
        print(name, phone)


def options():
    phone_book = {}
    while True:
        print("(1) Añadir contacto")
        print("(2) Eliminar Contacto")
        print("(3) Lista de Contactos")
        print("(4) Salir")
        option = int(input("Elige opción"))
        if option == 1:
            name = input("Tu nombre")
            phone = input("Telefono")
            add_contact(phone_book, name, phone)
        elif option == 2:
            name = input("Nombre del contacto")
        elif option == 3:
            list_contact(phone_book)
        elif option == 4:
            break
options()
