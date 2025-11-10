from validaciones import *

def crear_matriz(filas:int,columnas:int, valor = 0):
    matriz = [[valor] * columnas for i in range(filas)]   
    
    return matriz  

def ingreso_de_datos (vector_usuarios: list, vector_empresas: list, vector_precios: list) ->list:
    """ Pide al usuario ingreso de datos y los ingresa a una matriz

    Args:
        vector_usuarios (list): lista con todos los usuarios registrados
        vector_empresas (list): lista con las empresas disponibles
        vector_precios (list): lista con los precios de las acciones de las empresas

    Returns:
        list: retorna la matriz con los datos ingresados por el usuario
    """

    acciones = crear_matriz(15,3,0)
    usuario = validar_usuario(vector_usuarios, "Ingrese su nombre de usuario: ","Error... Reingrese su nombre de usuario: " )
    print(f"\nHola, Buenos dias señor/a {vector_usuarios[usuario]}\n")
    empresa = validar_usuario(vector_empresas,"Ingrese el nombre de la empresa que desea invertir (TESLA, APPLE, NVIDIA): ", "Error... Reingrese la empresa en la que desea invertir ( TESLA, APPLE, NVIDIA ): ")
    cant_acciones = get_int("Cuantas acciones desea comprar?: ", "Error, ingrese un entero del (1-500). Reingrese: ",0, 500)
    acciones[usuario][empresa] += cant_acciones
    print(f"\nUsted ha invertido US${cant_acciones * vector_precios[empresa]}")

    return acciones

def mostrar_lista (matriz: list) -> None:
    """Muestra una lista

    Args:
        matriz (list): lista que queres ingresar
    """
    for i in range(len(matriz)):        
        print(matriz[i])


def mostrar_matriz (matriz: list) -> None:
    """Muestra una matriz

    Args:
        matriz (list): matriz que queres mostrar
    """
    for i in range(len(matriz)):   
        for j in range(len(matriz[i])):     
            print(matriz[i][j], end = "")
        print()
        

def sumar_filas(matriz:list) -> list:
    """Suma filas de una matriz

    Args:
        matriz (list): matriz la cual queres sumar sus filas

    Returns:
        list: retorna una lista con la suma de cada fila
    """
    total_por_filas = [0] * len(matriz)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total_por_filas[i] += matriz[i][j]

    return total_por_filas


def sumar_columnas(matriz:list) -> list:
    """Suma columnas de una matriz

    Args:
        matriz (list): matriz la cual queres sumar sus columnas

    Returns:
        list: retorna una lista con la suma de cada columna
    """
    total_por_columnas = [0] * len(matriz[0])

    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            total_por_columnas[j] += matriz[i][j]

    return total_por_columnas


def cant_acciones_por_usuario (matriz:list, vector_usuarios:list) -> None:
    """Muestra la cantidad de acciones compradas por cada usuario

    Args:
        matriz (list): matriz con acciones compradas
        vector_usuarios (list): lista de usuarios registrados
    """
    vector_acciones = sumar_filas(matriz)
    for i in range (len(vector_acciones)):
        print(f"{vector_usuarios[i]:<16} ha comprado {vector_acciones[i]} accion/es")


def promedio_acciones_por_empresa (matriz:list) ->list:
    """Calcula el promedio de acciones de cada empresa

    Args:
        matriz (list): matriz de acciones compradas

    Returns:
        list: retorna una lista con el promedio de acciones de cada empresa
    """
    vector = sumar_columnas(matriz)
    vector_promedios_por_empresa = []

    for j in range(len(matriz[0])):
        contador = 0
        for i in range(len(matriz)):
            if matriz[i][j] > 0:
                contador += 1
        if contador == 0:
            vector_promedios_por_empresa += [contador]
        else:
            promedio = vector[j] / contador
            vector_promedios_por_empresa += [promedio]

    return vector_promedios_por_empresa

def mostrar_promedio_acciones_por_empresa (matriz:list,vector_empresas:list) -> None:
    """Muestra las empresas con su promedio de acciones

    Args:
        matriz (list): matriz de acciones compradas 
        vector_empresas (list): lista con las empresas disponibles
    """
    vector_promedios_por_empresa = promedio_acciones_por_empresa(matriz)

    for i in range(len(matriz[0])):
        print(f"El promedio de las acciones de {vector_empresas[i]:<6} es de: {vector_promedios_por_empresa[i]} ")


def swap (vector:list, i: str|int, j: str|int) -> None:
    """Intercambia elementos dentro de una lista ordenadamente

    Args:
        vector (list): lista que desea ordenar
        i (str | int): posición del primer elemento(i)
        j (str | int): posición del segundo elemento(j)
    """
    auxiliar = vector[i]
    vector[i] = vector[j]
    vector[j] = auxiliar

    
def suma_total_invertido_matriz(matriz: list, vector_precios: list) -> int:
    """Suma total de las inversiones de todos los usuarios

    Args:
        matriz (list): matriz de acciones compradas
        vector_precios (list): lista de precios de las empresas

    Returns:
        int: retorna el valor de las acciones totales invertidas
    """
    total = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total += matriz[i][j] * vector_precios[j]
    return total


def calcular_matriz_total_invertido(matriz: list, vector_precios: list) -> list:
    """Calcula el valor de las acciones por empresa y por usuario y los devuelve a la matriz

    Args:
        matriz (list): matriz de acciones compradas
        vector_precios (list): lista de precios de las acciones 

    Returns:
        list: retorna una matriz con el valor en US$ de las acciones compradas
    """
    matriz_total = [[0] * len(matriz[0]) for i in range(len(matriz))] 

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz_total [i][j] = matriz [i][j] * vector_precios [j] 
            
    return matriz_total


def accion_con_mayor_o_menor_inversion(matriz: list, vector_precios: list, mayor_recaudacion: bool ) -> int:
    """Calcula la empresa que mas o menos dinero recaudó

    Args:
        matriz (list): matriz de acciones compradas
        vector_precios (list): lista de precios de las acciones de las empresas
        mayor_recaudacion (bool): True: para calcular que que empresa recaudó mas| False: para calcular que que empresa recaudó menos

    Returns:
        int: retorna el indice de la empresa del vector_empresas que mas o menos dinero recaudó
    """
    matriz_total_inversiones = calcular_matriz_total_invertido(matriz, vector_precios)
    vector_suma = sumar_columnas(matriz_total_inversiones)

    maximo = vector_suma[0]
    indice_maximo = 0

    for i in range(len(vector_suma)):
        if mayor_recaudacion == True:
            if vector_suma[i] > maximo:
                maximo = vector_suma[i]
                indice_maximo = i
        else:
            if vector_suma[i] < maximo:
                maximo = vector_suma[i]
                indice_maximo = i

    return indice_maximo


def ordenar_matriz_alfabeticamente_a_z(matriz: list, vector_usuarios: list, bandera = True) -> list:
    """Ordena una matriz en orden alfabetico segun los usuarios

    Args:
        matriz (list): matriz de acciones compradas
        vector_usuarios (list): lista de usuarios registrados
        bandera (bool, optional): True: para ordenar de "a" a "z" y False para ordenar de "z" a "a". Defaults to True.

    Returns:
        list: retorna una matriz ordenada
    """
    for i in range(0, len(vector_usuarios) -1 , 1):
        for j in range(i+1 , len(vector_usuarios), 1):
            if bandera == True:
                if vector_usuarios[i] > vector_usuarios[j]:
                    swap(vector_usuarios, i , j)
                    swap(matriz, i , j)
            else:
                if vector_usuarios[i] < vector_usuarios[j]:
                    swap(matriz, i , j)
                    swap(vector_usuarios, i , j)
    return matriz


def ordenar_filas_alfabeticamente_z_a(matriz: list, vector_usuarios: list) -> list:
    """Calcula en un vector la suma de sus acciones en orden alfabetico

    Args:
        matriz (list): matriz de acciones compradas
        vector_usuarios (list): lista de usuarios registrados

    Returns:
        list: retorna una lista con la suma de las acciones de los usuarios en orden alfabetico
    """
    vector_suma_acciones = sumar_filas(matriz)
    for i in range(0, len(vector_usuarios) -1 , 1):
        for j in range(i+1 , len(vector_usuarios), 1):
            if vector_usuarios[i] < vector_usuarios[j]:

                swap(vector_usuarios, i , j)
                swap(matriz, i , j)
                swap(vector_suma_acciones, i , j)

    return vector_suma_acciones


def ordenar_filas_alfabeticamente_a_z(matriz: list, vector_usuarios: list) -> list:
    """Calcula en un vector la suma de sus acciones en orden alfabetico

    Args:
        matriz (list): matriz de acciones compradas
        vector_usuarios (list): lista de usuarios registrados

    Returns:
        list: retorna una lista con la suma de las acciones de los usuarios en orden alfabetico
    """
    vector_suma_acciones = sumar_filas(matriz)
    for i in range(0, len(vector_usuarios) -1 , 1):
        for j in range(i+1 , len(vector_usuarios), 1):
            if vector_usuarios[i] > vector_usuarios[j]:

                swap(vector_usuarios, i , j)
                swap(matriz, i , j)
                swap(vector_suma_acciones, i , j)

    return vector_suma_acciones


def ordenar_alfabeticamente_con_el_total_invertido(matriz: list, vector_precios: list,vector_usuarios: list) -> None:
    """Muestra usuarios alfabeticamente junto al total invertido

    Args:
        matriz (list): matriz de acciones compradas
        vector_precios (list): lista de precios de las acciones
        vector_usuarios (list): lista de usuarios registrados
    """
    matriz_inversiones = calcular_matriz_total_invertido(matriz, vector_precios)
    vector_suma_acciones = ordenar_filas_alfabeticamente_z_a(matriz_inversiones, vector_usuarios)
    
    for i in range(len(vector_usuarios)):
        print(f"{vector_usuarios[i]:<16} ha invertido US$ {vector_suma_acciones[i]}")

def ordenar_filas_alfabeticamente_usuarios(vector_usuarios: list) -> list:
    """Ordena usuarios alfabeticamente

    Args:
        vector_usuarios (list): lista de usuarios registrados

    Returns:
        list: retorna una lista ordenada de los usuarios
    """
    
    for i in range(0, len(vector_usuarios) -1 , 1):
        for j in range(i+1 , len(vector_usuarios), 1):
            if vector_usuarios[i] > vector_usuarios[j]:
                swap(vector_usuarios, i , j)

    return vector_usuarios


def porcentaje_de_inversion(matriz: list, vector_precios: list) -> list:
    """Calcula el porcentaje de inversion por usuario

    Args:
        matriz (list): matriz de acciones compradas
        vector_precios (list): lista de precios de las acciones

    Returns:
        list: retorna en una lista el porcentaje de inversion por usuario
    """

    inversion_total = suma_total_invertido_matriz(matriz, vector_precios)
    matriz_inversion_por_usuario = calcular_matriz_total_invertido(matriz, vector_precios)

    for i in range(len(matriz_inversion_por_usuario)):
        for j in range(len(matriz_inversion_por_usuario[i])):
            matriz_inversion_por_usuario [i][j] = (matriz_inversion_por_usuario [i][j]) * 100 / inversion_total
        
    return matriz_inversion_por_usuario


def porcentaje_de_inversion_por_usuario(matriz: list, vector_precios: list, vector_usuarios: list) -> None:
    """Muestra el porcentaje de inversión por usuario respecto a la inversión total acumulada

    Args:
        matriz (list): matriz de acciones compradas
        vector_precios (list): lista de precios de las acciones
        vector_usuarios (list): lista de usuarios registrados
    """
    inversion_total = suma_total_invertido_matriz(matriz, vector_precios)
    
    for i in range(len(matriz)):
        total_usuario = 0
        for j in range(len(matriz[i])):
            total_usuario += matriz[i][j] * vector_precios[j]
        
        porcentaje = total_usuario * 100 / inversion_total
        print(f"Al usuario {vector_usuarios[i]:<16} le corresponde el % {porcentaje:.2f}")


def compra_mayor_de_acciones_por_usuario (matriz: list, vector_usuarios: list, vector_empresas: list) -> None:
    """Muestra los usuarios con la empresa en la que mas inversiones compro

    Args:
        matriz (list): matriz de acciones compradas
        vector_usuarios (list): lista de usuarios registrados
        vector_empresas (list): lista con las empresas disponibles
    """
    
    
    for i in range(len(matriz)):
        maximo = 0
        indice_maximo = -1
        for j in range (len(matriz[i])):
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]
                indice_maximo = j  
        if indice_maximo !=-1:
            print(f"{vector_usuarios[i]:<16} {vector_empresas[indice_maximo]}")
        else:
            print(f"{vector_usuarios[i]:<16} Ninguna")


def visualizar_todos_los_datos(matriz_acciones: list, vector_usuarios: list,vector_empresas: list,vector_precios: list) -> None:
    """Muestra los datos de los usuarios que han comprado acciones

    Args:
        matriz_acciones (list): matriz de acciones compradas
        vector_usuarios (list): lista de usuarios registrados
        vector_empresas (list): lista con las empresas disponibles
        vector_precios (list): lista de precios de las acciones 
    """
    ordenar_filas_alfabeticamente_a_z(matriz_acciones,vector_usuarios)
    for i in range(len(matriz_acciones)):
        for j in range(len(matriz_acciones[i])):
            if matriz_acciones[i][j] != 0:
                print(f"\n● Usuario: {vector_usuarios[i]}\n● Acción: {vector_empresas[j]}\n● Precio por unidad: {vector_precios[j]}\n● Cantidad adquirida: {matriz_acciones[i][j]}\n● Total invertido: {(matriz_acciones[i][j]) * vector_precios[j]}\n ")


def total_por_usuarios(matriz: list, vector_precios: list) -> list:
    """Calcula el dinero invertido que tiene cada usuario

    Args:
        matriz (list): matriz de acciones compradas
        vector_precios (list): lista de precios de las acciones 

    Returns:
        list: retorna una lista del dinero invertido por cada usuario
    """
    total_por_usuario = [0] * len(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total_por_usuario[i] += matriz[i][j] * vector_precios[j]

    return total_por_usuario


def promedio_general_inver(matriz: list, vector_precios: list) -> int:
    """Calcula el promedio del dinero invertido por todos los usuarios

    Args:
        matriz (list): matriz de acciones compradas
        vector_precios (list): lista de precios de las acciones 

    Returns:
        int: retorna el promedio del dinero invertido por todos los usuarios en numero entero 
    """
    total_por_usuario = total_por_usuarios(matriz, vector_precios)
    acumulador_total = 0
    usuarios_que_invirtieron = 0
    for i in range(len(total_por_usuario)):
        if total_por_usuario[i] !=0:
            acumulador_total += total_por_usuario[i]
            usuarios_que_invirtieron += 1

    promedio_general = acumulador_total / usuarios_que_invirtieron 

    return promedio_general


def usuarios_superiores_al_promedio(matriz: list,vector_usuarios: list, vector_precios: list) -> None:
    """Muestra a los usuarios con dinero invertido superior al promedio

    Args:
        matriz (list): matriz de acciones compradas
        vector_usuarios (list): lista de usuarios registrados
        vector_precios (list): lista de precios de las acciones 
    """

    total_por_usuario = total_por_usuarios(matriz, vector_precios)
    promedio_general = promedio_general_inver(matriz, vector_precios)

    print(f"Promedio general de inversiones: US${promedio_general:.2f} \n")
    print("Usuarios con promedio superior al general:")
    for i in range(len(matriz)):
        promedio_usuario = total_por_usuario[i] 
        if promedio_usuario > promedio_general:
            print(f"{vector_usuarios[i]:<16} - Total invertido: ${promedio_usuario:.2f}")


def usuarios_superiores_al_promedio_de_x_empresa (matriz: list,vector_usuarios: list, vector_empresas: list, empresa: str) -> None:
    """ Muestra a los usuarios con acciones superior al promedio de (x) empresa

    Args:
        matriz (list): matriz de acciones compradas
        vector_usuarios (list): lista de usuarios registrados
        vector_empresas (list): lista de empresas disponibles
        empresa (str): empresa la cual se quiere hacer el promedio, por ej:("TESLA)
    """
    NOMBRE_DE_EMPRESA = empresa
    vector_promedios_por_empresa = promedio_acciones_por_empresa(matriz)
    for i in range (len(vector_empresas)):
        if vector_empresas[i] == empresa:
            empresa = i
            
    vector_usuarios_superiores_al_promedio = []
    vector_nombre_usuarios_superiores_al_promedio = []
    for i in range(len(matriz)):
        if matriz[i][empresa] >= vector_promedios_por_empresa[empresa]:
            vector_usuarios_superiores_al_promedio += [matriz[i][empresa]]
            vector_nombre_usuarios_superiores_al_promedio += [vector_usuarios[i]]

    for i in range (0,len(vector_usuarios_superiores_al_promedio)-1 , 1):
        for j in range( i+1, len(vector_usuarios_superiores_al_promedio),1 ):
            if vector_usuarios_superiores_al_promedio[i] < vector_usuarios_superiores_al_promedio[j]:
                swap(vector_usuarios_superiores_al_promedio,i,j)
                swap(vector_nombre_usuarios_superiores_al_promedio,i,j)

    print(f"\nPROMEDIO DE ACCIONES DE {NOMBRE_DE_EMPRESA}: {vector_promedios_por_empresa[empresa]}\n")
    print("Usuarios con promedio de acciones superior al general:")
    for i in range(len(vector_usuarios_superiores_al_promedio)):
        print(f"{vector_nombre_usuarios_superiores_al_promedio[i]:<16} {vector_usuarios_superiores_al_promedio[i]:<2} acciones")