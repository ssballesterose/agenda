
agenda = {}


def agregar_contacto():
	print('Agregar contacto')

	
def remover_contacto():
	"""Función remover contacto"""
	nombre = input('Nombre del contacto: ')
	try:
		del (agenda[nombre])
	except KeyError:
		'Ese contacto no existe'
	else:
		print('Contacto eliminado')
	

def actualizar_contacto():
	"""Función actualizar contacto"""
	
	
def ver_contacto():


def ver_todos():


print('Bienvenido a la agenda')
while True:
    print('1 - Agregar contacto')
    print('2 - Remover contacto')
    print('3 - Actualizar contacto')
    print('4 - Ver un contacto')
    print('5 - Ver todos los contactos')
    print('6 - Salir')
    try:
        op = int(input('Seleccione operacion: '))
    except ValueError:
        print('Ingrese un numero')
    else:
        if op == 1:
            agregar_contacto()
        elif op == 2:
            remover_contacto()
        elif op == 3:
            actualizar_contacto()
        elif op == 4:
            ver_contacto()
        elif op == 5:
            ver_todos()
        else:
            break
