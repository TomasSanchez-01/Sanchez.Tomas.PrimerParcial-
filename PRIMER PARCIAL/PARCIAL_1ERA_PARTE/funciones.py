from validaciones import *


# COLUMNAS = EMPRESAS
# FILAS    = USUARIOS
# matriz_acciones =  [
#     [0,1,0],
#     [1,3,5],
#     [2,3,5],
#     [3,3,5],
#     [4,3,5],
#     [5,3,5],
#     [6,3,5],
#     [7,3,5],
#     [8,3,5],
#     [9,3,5],
#     [10,3,5],
#     [11,3,5],
#     [12,3,5],
#     [13,3,5],
#     [14,3,5],
# ]

def ingreso_de_datos (vector_usuarios, vector_empresas, vector_precios):
    
    acciones = crear_matriz(15,3,0)

    usuario = validar_usuario(vector_usuarios, "Ingrese su nombre de usuario: ","Error... Reingrese su nombre de usuario: " )

    empresa = validar_usuario(vector_empresas,"Ingrese el nombre de la empresa que desea invertir: ", "Error... Reingrese la empresa en la que desea invertir: ")

    cant_acciones = get_int("Cuantas acciones desea comprar?: ", "Error, se podrán comprar en un rango de (1-20). Reingrese: ",0, 500)
    
    acciones[usuario][empresa] += cant_acciones
    print(f"\nUsted ha invertido US${cant_acciones * vector_precios[empresa]}")

    return acciones
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


def cant_acciones_por_usuario (matriz, vector_usuarios):
    vector_acciones = sumar_filas(matriz)
    for i in range (len(vector_acciones)):
        print(f"{vector_usuarios[i]} ha comprado {vector_acciones[i]} accion/es")

def promedio_acciones_por_empresa (matriz:list, vector_empresas: list):
    vector = sumar_columnas(matriz)
    for i in range(len(vector)):
        if vector[i] > 0:
            promedio = vector[i] / len(matriz) 
            print(f"El promedio de las acciones de {vector_empresas[i]} es de: {promedio} ")


def suma_total_invertido_matriz(matriz: list, vector_precios) -> int:
    total = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total += matriz[i][j] * vector_precios[j]
    return total


def calcular_matriz_total_invertido(matriz, vector_precios) -> list:
    matriz_total = [[0] * len(matriz[0]) for i in range(len(matriz))] 

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz_total [i][j] = matriz [i][j] * vector_precios [j] 
    return matriz_total


def accion_con_mayor_inversion(matriz, vector_precios,vector_empresas):
    matriz_total_inversiones = calcular_matriz_total_invertido(matriz, vector_precios)
    vector_suma = sumar_columnas(matriz_total_inversiones)

    maximo = vector_suma[0]
    indice_maximo = 0

    for i in range(1, len(vector_suma)):
        if vector_suma[i] > maximo:
            maximo = vector_suma[i]
            indice_maximo = i
        
    return indice_maximo


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

def ordenar_filas_alfabeticamente_a_z(matriz, vector_usuarios):
    vector_suma_acciones = sumar_filas(matriz)
    for i in range(0, len(vector_usuarios) -1 , 1):
        for j in range(i+1 , len(vector_usuarios), 1):
            if vector_usuarios[i] > vector_usuarios[j]:

                swap(vector_usuarios, i , j)
                swap(matriz, i , j)
                swap(vector_suma_acciones, i , j)

    return vector_suma_acciones

def ordenar_alfabeticamente_con_el_total_invertido(matriz, vector_precios,vector_usuarios):
    matriz_inversiones = calcular_matriz_total_invertido(matriz, vector_precios)
    vector_suma_acciones = ordenar_filas_alfabeticamente_z_a(matriz_inversiones, vector_usuarios)
    mostrar_datos(vector_usuarios, vector_suma_acciones)


def porcentaje_de_inversion(matriz, vector_precios):

    inversion_total = suma_total_invertido_matriz(matriz, vector_precios)
    matriz_inversion_por_usuario = calcular_matriz_total_invertido(matriz, vector_precios)

    for i in range(len(matriz_inversion_por_usuario)):
        for j in range(len(matriz_inversion_por_usuario[i])):
            matriz_inversion_por_usuario [i][j] = (matriz_inversion_por_usuario [i][j]) * 100 / inversion_total
        
    return matriz_inversion_por_usuario


def porcentaje_de_inversion_por_usuario(matriz, vector_precios, vector_usuarios):

    inversion_total = suma_total_invertido_matriz(matriz, vector_precios)
    
    for i in range(len(matriz)):
        total_usuario = 0
        for j in range(len(matriz[i])):
            total_usuario += matriz[i][j] * vector_precios[j]
        
        porcentaje = total_usuario * 100 / inversion_total
        print(f"Al usuario {vector_usuarios[i]:<16} le corresponde el %{porcentaje:.2f}")


def compra_mayor_de_acciones_por_usuario (matriz, vector_usuarios, vector_empresas):
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
        
def promedio_general_inversiones (matriz,vector_precios) -> int:
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total += matriz[i][j] * vector_precios[j]
    promedio_general = total / len(matriz)

    return promedio_general


def visualizar_todos_los_datos(matriz_acciones, vector_usuarios,vector_empresas,vector_precios):
    ordenar_filas_alfabeticamente_a_z(matriz_acciones,vector_usuarios)
    for i in range(len(matriz_acciones)):
        for j in range(len(matriz_acciones[i])):
            if matriz_acciones[i][j] != 0:
                print(f"\n● Usuario: {vector_usuarios[i]}\n● Acción: {vector_empresas[j]}\n● Precio por unidad: {vector_precios[j]}\n● Cantidad adquirida: {matriz_acciones[i][j]}\n● Total invertido: {(matriz_acciones[i][j]) * vector_precios[j]}\n ")




def total_por_usuarios(matriz, vector_precios):
    total_por_usuario = [0] * len(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total_por_usuario[i] += matriz[i][j] * vector_precios[j]

    return total_por_usuario

def promedio_general_inver(matriz, vector_precios):
    total_por_usuario = total_por_usuarios(matriz, vector_precios)
    acumulador_total = 0
    for i in range(len(total_por_usuario)):
        if total_por_usuario[i] !=0:
            acumulador_total += total_por_usuario[i]

    promedio_general = acumulador_total / len(total_por_usuario)

    return promedio_general

def usuarios_superiores_al_promedio(matriz,vector_usuarios, vector_precios):

    total_por_usuario = total_por_usuarios(matriz, vector_precios)
    promedio_general = promedio_general_inver(matriz, vector_precios)

    print(f"Promedio general de inversiones: US${promedio_general:.2f} \n")
    print("Usuarios con promedio superior al general:")
    for i in range(len(matriz)):
        promedio_usuario = total_por_usuario[i] 
        if promedio_usuario > promedio_general:
            print(f"{vector_usuarios[i]:<16} - Total invertido: ${promedio_usuario:.2f}")