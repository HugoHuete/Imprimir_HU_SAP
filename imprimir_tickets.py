from pynput import keyboard, mouse
from time import sleep
from helper import cambiar_pestaña, clickear

def main():
    coordenadas_usuarios ={"Usuario1":{
                                    "Linea1":(449, 364),
                                    "Linea2":(449, 381),
                                    "Ejecutar": (58,155),
                                    "Repetir": (83,155)},

                            "Usuario2":
                                    {"Linea1":(480, 357),
                                    "Linea2":(480, 376),
                                    "Ejecutar": (65,163),
                                    "Repetir": (91,162)},
                            "Usuario3":
                                    {"Linea1":(463, 335),
                                    "Linea2":(464, 353),
                                    "Ejecutar": (57,155),
                                    "Repetir": (80,155)}
                            }
    usuarios = ["Usuario1", "Usuario2", "Usuario3"]
    num_usuario = int(input("\n\nSeleccione su usuario: \n" +
            "0. Hugo\n" +
            "1. Jasely\n" + 
            "2. Jorge\n\n" +
            "Selección: "))
    coordenadas = coordenadas_usuarios[usuarios[num_usuario]]

    # Solicita posicionar pestaña SAP y teclear Y para confirmar ejecución.
    if not confirmar_ejecucion():
        return

    cant_tickets = int(input("\n\nIngrese la cantidad de HUS: "))
    print("\nCantidad de impresiones por ticket: \n" +
        "1. Imprimir 2 ticket por HU.\n" + 
        "2. Imprimir la primera 2 veces y luego imprimir el resto solo 1 vez.\n" + 
        "3. Imprimir la ultima 2 veces y el resto solo 1 vez.\n" +
        "4. Imprimir 1 ticket por HU.")
    opcion = int(input("Ingrese la opción a seleccionar (1-4): "))

    
    imprimir(coordenadas, cant_tickets, opcion)
        
    
# ---------------------------------------------------------------------------------------------------


def confirmar_ejecucion():
    print("\n Pasos previos: \n1. Usar ctrl+tab para seleccionar la pantalla SAP para imprimir tickets.\n2. Regresar a python.")
    respuesta = input("Presiona Y para continuar o cualquier tecla para cancelar: ")

    if respuesta not in ("Y", "y"):
        return False
    return True


def imprimir(coordenadas, cant_tickets, opcion):
    cambiar_pestaña(teclado,keyboard.Key)
    sleep(1)
    for i in range(cant_tickets):
        imprimir_primera(coordenadas) # Siempre hay que imprimir la primera
        print(f'primera {i}')

        # Imprimir la primera 2 veces si es opcion 2
        # Imprimir la ultima 2 veces si es opcion 3
        if (i == 0 and opcion == 2) or (i == (cant_tickets -1) and opcion == 3):
            print(f'Segunda {i}, {cant_tickets}')
            imprimir_segunda(coordenadas)

        # Si es opcion 4 siempre imprimir la 2da ticket
        if opcion == 1:
            imprimir_segunda(coordenadas)

        # ctrl + s
        guardar()
    

def imprimir_primera(coordenadas):
    sleep(1)
    raton.position = coordenadas["Linea1"]
    sleep(1)
    clickear(raton, click_izq)
    raton.position = coordenadas["Ejecutar"]
    clickear(raton, click_izq)
    sleep(11)

def imprimir_segunda(coordenadas):
    raton.position = coordenadas["Linea1"]
    clickear(raton, click_izq)
    sleep(1)
    raton.position = coordenadas["Repetir"]
    clickear(raton, click_izq)
    sleep(1)
    raton.position = coordenadas["Linea2"]
    clickear(raton, click_izq)
    sleep(1)
    raton.position = coordenadas["Ejecutar"]
    clickear(raton, click_izq)
    sleep(11)

def guardar():
    with teclado.pressed(keyboard.Key.ctrl):
        teclado.press('s')
        teclado.release('s')


teclado = keyboard.Controller()
raton = mouse.Controller()
click_izq = mouse.Button.left

if  __name__ == "__main__":
    main()

