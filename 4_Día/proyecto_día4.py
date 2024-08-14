agenda = {}
print("Agenda de contactos")
print("1.Añadir contacto")
print("2.Buscar contacto")
print("3.Editar contacto")
print("4.Eliminar contacto")
print("5.Mostrar contactos")
eleccion = input("Elige una opción: ")
if eleccion == "1":
    nombre = input("Escribe el nombre del contacto: ")
    telefono = input("Escribe el telefono del contacto: ")
    agenda[nombre] = telefono
    print("Se creo el contacto")
elif eleccion == "2":
    nombre = input("Nombre del contacto: ")
    if nombre in agenda:
        print(f"El telefono de {nombre} es {agenda[nombre]}")
    else:
        print("Ese contacto no existe")
elif eleccion == "3":
    nombre = input("Nombre del contacto: ")
    if nombre in agenda:
        nuevoNum = input("Ingrese el nuevo numero")
        agenda[nombre] = nuevoNum
        print(f"Se actualizó el numero de {nombre} a {agenda[nombre]}")
    else:
        print("Ese contacto no existe")
elif eleccion == "4":
    nombre = input("Nombre del contacto: ")
    if nombre in agenda:
        agenda.pop(nombre)
        print(f"El contacto fue eliminado")
    else:
        print("Ese contacto no existe")
elif eleccion == "5":
    print(agenda)
else:
    print("Opción inválida")