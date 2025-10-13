
def validate_number(numero: int, minimo:int, maximo:int) -> bool:
    numero_validado = True
    if numero < minimo or numero > maximo:
        numero_validado = False

    return numero_validado

def get_int( mensaje: str, mensaje_error: str , minimo: int , maximo: int) -> int|None:
    
    numero = int(input(mensaje))
    
    while not validate_number(numero, minimo, maximo):
        numero = int(input(mensaje_error))

    return numero 


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