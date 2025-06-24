# Menú de administración de contactos en memoria

contactos = []

def agregar_contacto():
    nombre = input("Ingrese nombre: ")
    telefono = input("Ingrese teléfono: ")
    email = input("Ingrese email: ")
    contacto = {"nombre": nombre, "telefono": telefono, "email": email}
    contactos.append(contacto)
    print("Contacto agregado exitosamente.\n")

def buscar_contacto():
    nombre = input("Ingrese el nombre a buscar: ")
    encontrados = [c for c in contactos if c["nombre"].lower() == nombre.lower()]
    if encontrados:
        for c in encontrados:
            print(f"Nombre: {c['nombre']}, Teléfono: {c['telefono']}, Email: {c['email']}")
    else:
        print("Contacto no encontrado.\n")

def mostrar_contactos():
    if not contactos:
        print("No hay contactos registrados.\n")
        return
    for idx, c in enumerate(contactos, start=1):
        print(f"{idx}. Nombre: {c['nombre']}, Teléfono: {c['telefono']}, Email: {c['email']}")
    print()

def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    global contactos
    antes = len(contactos)
    contactos = [c for c in contactos if c["nombre"].lower() != nombre.lower()]
    if len(contactos) < antes:
        print("Contacto eliminado exitosamente.\n")
    else:
        print("Contacto no encontrado.\n")

def menu():
    while True:
        print("=== Menú de Administración de Contactos ===")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos los contactos")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            mostrar_contactos()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente nuevamente.\n")

# Iniciar menú
menu()
