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

        print("\n1. Registrar una transacción.\n2. Visualizar todos los datos.\n3. Consultas.\n4. Salir")
        opcion = get_int("\nIngrese una opción: ", "Error, Reingrese una opción (1-4): ",1,4 )
        match opcion:
            case 1:
                nueva_matriz = ingreso_de_datos(vector_usuarios, vector_empresas, vector_precios)
                for i in range(len(matriz_acciones)):
                    for j in range(len(matriz_acciones[i])):
                        matriz_acciones[i][j] += nueva_matriz[i][j]
            case 2:
                print("\n----------------LISTA DE USUARIOS INGRESADOS----------------")
                visualizar_todos_los_datos(matriz_acciones, vector_usuarios,vector_empresas,vector_precios)
            case 3:
                submenu(matriz_acciones, vector_usuarios,vector_empresas,vector_precios)
            case 4:
                print("\nSaliendo del programa...\n")
                bandera = False

def submenu(matriz_acciones, vector_usuarios, vector_empresas, vector_precios):

    bandera = True
    while bandera == True:
        print("\n----------------CONSULTAS----------------\n")
        print("1. Cantidad de acciones de cada usuario.\n2. Promedio de acciones adquiridas por cada empresa.\n3. Total invertido de cada usuario ordenado alfabeticamente z-a.\n4. Inversiones totales en la app.\n5. Por cada usuario, la empresa en la que compró más acciones.\n6. Acción con mayor inversión total (USD) en toda la cartera.\n7. Porcentaje de inversión por usuario respecto a la inversión total acumulada.\n8. Listado de los usuarios cuyo promedio del total de sus inversiones supere el promedio del total de inversiones de toda la cartera.\n9. Determinar cuál es la empresa que menos dinero recaudó.\n10. Todos los usuarios cuya cantidad de acciones de Tesla supere el número promedio de acciones de Tesla.\n11. Muestra para cada empresa cuál es el usuario que realizó la mayor inversión.\n12. Volver al menú principal.\n")
        opcion = get_int("Ingrese una opción: ", "Error, Reingrese una opción (1-12): ",1,12 )
        match opcion:
            case 1:
                print("\n---------- CANTIDAD TOTAL DE ACCIONES ADQUIRIDAS POR USUARIO ----------\n")
                cant_acciones_por_usuario(matriz_acciones, vector_usuarios)

            case 2:
                print("\n---------- PROMEDIO DE ACCIONES POR EMPRESA ----------\n")
                mostrar_promedio_acciones_por_empresa(matriz_acciones, vector_empresas)

            case 3:
                print("\n---------- USUARIOS JUNTO CON EL TOTAL INVERTIDO ----------\n")
                ordenar_alfabeticamente_con_el_total_invertido(matriz_acciones, vector_precios,vector_usuarios)

            case 4:
                print("\n---------- INVERSION TOTAL DE LA APP ----------\n")
                total = suma_total_invertido_matriz(matriz_acciones,vector_precios)
                print(f"Las inversiones totales en la app son de: US$ {total:.2F}")

            case 5:
                print("\n-------- USUARIO CON LA EMPRESA EN LA QUE MAS INVERSIONES COMPRÓ --------\n")
                compra_mayor_de_acciones_por_usuario(matriz_acciones,vector_usuarios, vector_empresas)

            case 6:
                print("\n---------- ACCIÓN CON MAYOR INVERSIÓN TOTAL ----------\n")
                maximo = accion_con_mayor_o_menor_inversion(matriz_acciones, vector_precios, True)
                print(f"La acción con mayor inversión total es: {vector_empresas[maximo]}")

            case 7:
                print("\n----- Porcentaje de inversión por usuario respecto a la inversión total acumulada -----\n")
                porcentaje_de_inversion_por_usuario(matriz_acciones, vector_precios, vector_usuarios)

            case 8:
                print("\n----- USUARIOS CON INVERSION MAYOR AL PROMEDIO -----\n")
                usuarios_superiores_al_promedio(matriz_acciones,vector_usuarios, vector_precios)

            case 9:
                print("\n---------- ACCIÓN CON MENOR INVERSIÓN TOTAL ----------\n")
                menor = accion_con_mayor_o_menor_inversion(matriz_acciones, vector_precios, False)
                print(f"La acción con menor inversión total es: {vector_empresas[menor]}")

            case 10:
                print("\n---------- USUARIOS CUYA CANTIDAD DE ACCIONES DE TESLA SUPERE EL NUMERO PROMEDIO----------\n")
                usuarios_superiores_al_promedio_de_x_empresa (matriz_acciones,vector_usuarios, vector_empresas, "TESLA")

            case 11:
                print("\n---------- USUARIOS QUE REALIZARON MAYOR INVERSION EN CADA EMPRESA----------\n")
                usuario_con_mayor_inversion_en_las_empresas(matriz_acciones,vector_usuarios,vector_empresas)
            case 12:
                print("\nVolviendo al menú principal...\n")
                bandera = False
                break

if __name__ == "__main__":
    main()