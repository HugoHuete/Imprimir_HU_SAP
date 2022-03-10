from pyautogui import click, pixel, pixelMatchesColor, hotkey, screenshot, locate, keyDown, press, keyUp
from time import sleep
from PIL import Image

def main():

    # Consultar cantidad de tickets y modo de imprimir
    cant_tickets = get_int("\n\nIngrese la cantidad de HUS: ")
    print("\nCantidad de impresiones por ticket: \n" + 
        "1. Imprimir 2 ticket por HU.\n" + 
        "2. Imprimir la primera 2 veces y luego imprimir el resto solo 1 vez.\n" + 
        "3. Imprimir la ultima 2 veces y el resto solo 1 vez.\n" +
        "4. Imprimir 1 ticket por HU.")
    opcion = get_int("Ingrese la opción a seleccionar (1-4): ")

    # Prepararse para que el programa, al cambiar de pestaña, caiga en el ventana correcta.
    input("\n*********** Buscar la pestaña que contiene la pantalla de impresión de tickets. Luego regresar a esta ventana y presionar enter.***********\n¿Listo? ")

    alt_tab()

    # Tomar screenshot para buscar algunos elementos usando locate
    im1 = screenshot()

    # Calcular las posiciones de los 2 botones usando como referencia la imagen de los 2 botones
    left, top, width, height = locate("imagenes\\botones_a_usar.png", im1, grayscale = True)
    boton_ejecutar = (int(left + 0.25 * width), int(top + height / 2))
    boton_sig_linea = (int(left + 0.75 * width), int(top + height / 2))

    # Calcular las posiciones de las 2 lineas usando como referencia la imagen de las lineas para imprimir
    left, top, width, height = locate("imagenes\\lineas_para_imprimir.png", im1, grayscale = True)
    primera_linea = (int(left + 0.5 * width), int(top + 0.375 * height))
    segunda_linea = (int(left + 0.5 * width), int(top + 0.625 * height))
    esquina_derecha = (int(left + 0.8 * width), int(top + 0.85 * height))

    # Verificar que locate haya retornado valores
    if boton_ejecutar == None or primera_linea ==  None:
        alt_tab()
        input("Hubo un error. Intentar de nuevo.")

    # Conseguir pixel verde de cuando se completo la impresión para comparaciones posteriores
    im2 = Image.open("imagenes\\icono_impresion_completada.png")
    pixel_verde = im2.getpixel((int(im2.width / 2), int(im2.height / 2)))
    pixel_amarillo = im1.getpixel(primera_linea)
    pixel_vacio = im1.getpixel((int(left + 0.8 * width), int(top + 0.625 * height)))

    # Iterar según la cantidad de tickets
    for ticket in range(cant_tickets):
        # Siempre se imprime la primera ticket, no importando la opcion escogida
        click_and_wait(primera_linea, 0.5)
        click_and_wait(boton_ejecutar, 3)
        wait_till_pixel(primera_linea, pixel_verde)
        sleep(0.4)

        # Imprimir segunda dependiendo de la opción seleccionada
        if opcion == 1 or (ticket == 0 and opcion == 2) or (ticket == cant_tickets - 1 and opcion == 3):
            click_and_wait(primera_linea, 0.5)
            click_and_wait(boton_sig_linea, 0.5)
            wait_till_pixel(esquina_derecha, pixel_vacio)
            sleep(0.5)
            click_and_wait(segunda_linea, 0.5)
            click_and_wait(boton_ejecutar, 3)
            wait_till_pixel(segunda_linea, pixel_verde)
            sleep(0.5)

        guardar()

        if ticket == cant_tickets - 1:
            return

        wait_till_pixel(primera_linea, pixel_amarillo)
        sleep(0.4)


def get_int(prompt):
    """
    Solicita al usuario que ingrese un entero. Repetira tantas veces como sea
    necesario hasta que el usuario ingrese un dato de tipo entero.
    """
    while True:
        try:
            return int(input(prompt))
        except:
            pass

def alt_tab():
    """
    Realiza la combinacion de alt + tab con un tiempo de espera.
    """
    hotkey("alt", "tab")
    sleep(1.5)

def click_and_wait(coordinates, seconds:int):
    """
    Combina las 2 funciones de click y sleep.
    """
    click(coordinates)
    sleep(seconds)

def wait_till_pixel(coordenada, pixel):
    """
    Compara el pixel de una coordenada dada con un pixel. No saldrá del bucle hasta que coincidan.
    """
    while not pixelMatchesColor(coordenada[0], coordenada[1], pixel):
        continue
    return

def guardar():
    keyDown('ctrl') # hold ctrl key
    press('s') # press s key
    keyUp('ctrl') # release ctrl key



if  __name__ == "__main__":
    main()

