import hangman
import reversegam
import tictactoeModificado

import json
import PySimpleGUI as sg

'''
La estructura almacenada en 'jugador.json' es un diccionario con dos campos, 
uno llamado 'jugador' que es otro diccionario generado con todos los datos
pedidos en la ventana de PySimpleGUI y el otro campo llamado 'juego' que es
un string con el nombre del juego seleccionado.
En el programa se pueden agregar y eliminar campos del jugador modificando
la lista 'datos' dentro de la funcion 'guardar_jugador'.
Elegi esta estructura porque hace que la informacion sobre los jugadores
sea dinamica y pueda cambiar de una version del programa a otra.
Utilizo json para guardar el archivo porque al ser un archivo de texto me
permite leerlo facilmente para depurar el programa y ademas permite abrir y
utilizar el archivo desde otros lenguajes de programacion.
'''

def mostrar_menu():
	layout = [
		[sg.Text('Elegí con qué juego querés jugar:')],
		[sg.Button('Ahorcado')],
		[sg.Button('Ta-Te-Ti')],
		[sg.Button('Otello')],
		[sg.Button('Salir')]
	]

	window = sg.Window('Juegos', layout)
	event, _ = window.read()
	window.close()

	if event is None:
		event = 'Salir'

	return event

def guardar_jugador(juego):
	datos = ['nombre', 'apellido', 'email', 'edad']

	layout = []
	layout.append([sg.Text('Ingrese sus datos:')])
	for dato in datos:
		layout.append([sg.Text(dato.capitalize()+':', size=(8, 1)), sg.Input(key=dato)])
	layout.append([sg.Submit(), sg.Cancel()])

	window = sg.Window('Jugador', layout)
	event, values = window.read()
	window.close()

	if event == 'Submit' and values['nombre']:
		jugador = {}
		for dato in datos:
			jugador[dato] = values[dato]
		
		datos_json = {
			'jugador': jugador,
			'ultimo_juego': juego
		}
		with open(jugador['nombre'].lower()+'.json', 'w') as f:
			json.dump(datos_json, f, indent=4)

def main(args):
	sigo_jugando = True
	while sigo_jugando:
		opcion = mostrar_menu()
		if opcion == 'Salir':
			sigo_jugando = False
		else:
			if opcion == 'Ahorcado':
				hangman.main()
			elif opcion == 'Ta-Te-Ti':
				tictactoeModificado.main()
			elif opcion == 'Otello':
				reversegam.main()
			guardar_jugador(opcion)
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
