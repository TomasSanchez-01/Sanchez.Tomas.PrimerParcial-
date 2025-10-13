from funciones import *

def main():
    vector_empresas = ["APPLE", "TESLA", "NVIDIA"]
    vector_precios = [10.41, 7.71, 8.50 ]
    vector_usuarios = [
    "Unatico_pixel",
    "Sombra_cristal", 
    "Ecoerrante",
    "Navefantasma",
    "Bytesdelabahia",
    "Tintaenelviento", 
    "Relojoxidado",
    "Miradacodificada",
    "Circuitoazul",
    "Fuego_niebla" ,
    "Teclaerrante",
    "Nebulosa_urbana",
    "Sueño_binario",
    "Saltofantasma", 
    "Claveoculta" ]
    matriz_acciones = [[0]*len(vector_empresas) for _ in range(len(vector_usuarios))]

    nueva_matriz = ingreso_de_datos(vector_usuarios, vector_empresas, vector_precios)
    for i in range(len(matriz_acciones)):
        for j in range(len(matriz_acciones[i])):
            matriz_acciones[i][j] += nueva_matriz[i][j]

    bandera = True
    while bandera == True:  

        print("1. Registrar una transacción.\n2. Visualizar todos los datos.\n3. Consultas.\n4. Salir")
        opcion = get_int("Ingrese una opción: ", "Error, Reingrese una opción (1-4): ",1,4 )
        match opcion:
            case 1:
                nueva_matriz = ingreso_de_datos(vector_usuarios, vector_empresas, vector_precios)
                for i in range(len(matriz_acciones)):
                    for j in range(len(matriz_acciones[i])):
                        matriz_acciones[i][j] += nueva_matriz[i][j]
            case 2:
                visualizar_todos_los_datos(matriz_acciones, vector_usuarios,vector_empresas,vector_precios)
            case 3:
                print("CONSULTAS")
                submenu(matriz_acciones, vector_usuarios,vector_empresas,vector_precios)
            case 4:
                print("Saliendo del programa.")
                bandera = False

def submenu(matriz_acciones, vector_usuarios, vector_empresas, vector_precios):

    bandera = True
    while bandera == True:
        print("\n1. Cantidad de acciones de cada usuario.\n2. Promedio de acciones adquiridas por cada empresa.\n3. Total invertido de cada usuario ordenado alfabeticamente z-a.\n4. Inversiones totales en la app.\n5. Por cada usuario, la empresa en la que compró más acciones.\n6. Acción con mayor inversión total (USD) en toda la cartera.\n7. Porcentaje de inversión por usuario respecto a la inversión total acumulada.\n8. Listado de los usuarios cuyo promedio del total de sus inversiones supere el promedio del total de inversiones de toda la cartera.\n9. Volver al menú principal.\n")
        opcion = get_int("Ingrese una opción: ", "Error, Reingrese una opción (1-9): ",1,9 )
        match opcion:
            case 1:
                cant_acciones_por_usuario(matriz_acciones, vector_usuarios)
            case 2:
                promedio_acciones_por_empresa(matriz_acciones, vector_empresas)
            case 3:
                ordenar_alfabeticamente_con_el_total_invertido(matriz_acciones, vector_precios,vector_usuarios)
            case 4:
                total = suma_total_invertido_matriz(matriz_acciones,vector_precios)
                print(f"Las inversiones totales en la app son de: {total}")
            case 5:
                compra_mayor_de_acciones_por_usuario(matriz_acciones,vector_usuarios, vector_empresas)
            case 6:
                maximo = accion_con_mayor_inversion(matriz_acciones, vector_precios,vector_empresas)
                print(f"La acción con mayor inversión total es: {vector_empresas[maximo]}")
            case 7:
                porcentaje_de_inversion_por_usuario(matriz_acciones, vector_precios, vector_usuarios)
            case 8:
                usuarios_superiores_al_promedio(matriz_acciones,vector_usuarios, vector_precios)
            case 9:
                print("Volviendo al menú principal.")
                bandera = False
                break

if __name__ == "__main__":
    main()