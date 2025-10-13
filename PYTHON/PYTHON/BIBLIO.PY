def crear_matriz(filas:int,columnas:int, valor):
    matriz = [[valor] * columnas for i in range(filas)]   
    
    return matriz  


def mostrar_lista (matriz: list):
    for i in range(len(matriz)):        
        print(matriz[i])


def mostrar_datos (vector_usuarios, vector_suma):
    for i in range(len(vector_usuarios)):
        print(f"{vector_usuarios[i]:>15} {vector_suma[i]}")


def mostrar_matriz (matriz: list):
    for i in range(len(matriz)):   
        for j in range(len(matriz[i])):     
            print(matriz[i][j], end = "")
        print()
        

def sumar_filas(matriz:list):
    total_por_filas = [0] * len(matriz)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total_por_filas[i] += matriz[i][j]

    return total_por_filas


def sumar_columnas(matriz:list):
    total_por_columnas = [0] * len(matriz[0])

    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            total_por_columnas[j] += matriz[i][j]

    return total_por_columnas

def swap (vector, i, j):
    auxiliar = vector[i]
    vector[i] = vector[j]
    vector[j] = auxiliar


def ordenar_filas_alfabeticamente_z_a(matriz, vector_usuarios):
    vector_suma_acciones = sumar_filas(matriz)
    for i in range(0, len(vector_usuarios) -1 , 1):
        for j in range(i+1 , len(vector_usuarios), 1):
            if vector_usuarios[i] < vector_usuarios[j]:

                swap(vector_usuarios, i , j)
                swap(matriz, i , j)
                swap(vector_suma_acciones, i , j)

    return vector_suma_acciones

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

""" 1️ Verificación de Cadena Alfabética """

def verificar_cadena ( cadena:str) -> bool:
    bandera = True
    if len(cadena) == 0:
        bandera = False

    for letra in range(len(cadena)):
        caracter = cadena[letra]
        if not ((caracter >= "A" and caracter <="Z") or (caracter >= "a" and caracter <= "z")):
            bandera = False

        if bandera == False:
            break

    return bandera


""" 2️⃣ Validación de Número Entero """

def verificacion_numero_entero (cadena_numero:str) -> bool:
    bandera = True

    if len(cadena_numero) == 0:
        bandera = False

    for i in range(len(cadena_numero)):
        caracter = cadena_numero[i]

        if i == 0 and (caracter == "+" or caracter == "-"):
            if len(cadena_numero) == 1:
                bandera = False

        elif  not ((caracter >= "0" and caracter <= "9")) :
            bandera = False

        if bandera == False:
            break
            

    return bandera


""" 3️⃣ Validación de Número Decimal """

def verificacion_numero_decimal (cadena_numero:str) -> bool:
    bandera = True
    punto = 0       
    digitos_antes = 0
    digitos_despues = 0
    punto_encontrado = False

    if len(cadena_numero) == 0:
        bandera = False

    for i in range(len(cadena_numero)):
        caracter = cadena_numero[i]

        if i == 0 and (caracter == "+" or caracter == "-"):
            if len(cadena_numero) == 1:
                bandera = False

        elif caracter == ".":
            punto += 1
            punto_encontrado = True
            if punto > 1:
                bandera = False

        elif (caracter >= "0" and caracter <= "9") :
            if punto_encontrado == False:
                digitos_antes += 1
            else:
                digitos_despues += 1
        else:
            bandera = False

        if bandera == False:
            break

    if punto == 1:
        if digitos_antes == 0 or digitos_despues == 0:
            bandera = False
    elif punto == 0:
        if digitos_antes == 0:
            bandera = False


    return bandera