
def validate_number(numero: int, minimo:int, maximo:int) -> bool:
    numero_validado = True
    if numero < minimo or numero > maximo:
        numero_validado = False

    return numero_validado

def es_entero(cadena):
    es_entero = True

    if len(cadena) == 0:
        es_entero = False

    if cadena[0] == "-":
        if len(cadena) == 1:
            es_entero = False
        cadena = cadena[1:]
    
    for i in range(len(cadena)):
        if cadena[i] < "0" or cadena[i] > "9":
            es_entero = False

    return es_entero

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int) -> int | None:
    numero = input(mensaje)

    while True:
        if numero == "":
            print("No ingresaste nada. Intenta de nuevo.")
            numero = input(mensaje_error)
            continue

        if not es_entero(numero):
            numero = input(mensaje_error)
            continue

        numero_int = int(numero)

        if not validate_number(numero_int, minimo, maximo):
            numero = input(mensaje_error)
            continue

        return numero_int


def validar_usuario(vector_usuario, mensaje, mensaje_error):

    usuario_encontrado = -1  
    usuario_ingresado = input(mensaje)

    while usuario_encontrado == -1:
        for i in range(len(vector_usuario)):
            if usuario_ingresado == vector_usuario[i]:
                usuario_encontrado = i
                break  

        if usuario_encontrado == -1: 
            usuario_ingresado = input(mensaje_error)

    return usuario_encontrado