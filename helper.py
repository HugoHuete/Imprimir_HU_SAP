

def cambiar_pestaña(teclado, key):
    """
    Recibe el controlador del teclado (keyboard.Controller()) y las llaves (Keyboard.key)
    Realiza un alt + tab para cambiar de pestaña
    """
    with teclado.pressed(key.alt):
        teclado.press(key.tab)
        teclado.release(key.tab)

def pegar(teclado, key):
    """
    Recibe el controlador del teclado (keyboard.Controller()) y las llaves (Keyboard.key)
    Realiza un ctrl + v para pegar del clipboard
    """
    with teclado.pressed(key.ctrl):
        teclado.press('v')
        teclado.release('v')

def clickear(raton, boton):
    """
    Recibe el controlador del mouse y el boton a presionar.
    """
    raton.press(boton)
    raton.release(boton)
