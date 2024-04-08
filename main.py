def menu():
    try:
        nromenu, edades = -1, []
        while nromenu != 0:
            print("Ingrese 1 para cargar listas de manera manual")
            print("Ingrese 2 para cargar datos desde un archivo")
            print("Ingrese 3 para mostrar lista")
            print("Ingrese 4 para calcular sumatoria")
            print("Ingrese 5 para calcular promedio")
            print("Ingrese 6 para mostrar edades mayores al promedio")
            print("Ingrese 7 para mostrar edad mayor numero")
            print("Ingrese 8 para mostrar edad menor numero")
            print("Ingrese 9 para mostrar la edad en letras")
            print("Ingrese 10 para ordenar en orden ascendente")
            print("Ingrese 11 para ordenar en orden descendente")
            print("Ingrese 12 para mostrar la diferencia entre cada edad y el promedio")
            print("Ingrese 13 para registrar los datos obtenidos en un archivo")
            print("Ingrese 0 para cerrar el programa\n")
            nromenu = input()
            if nromenu.isnumeric():
                nromenu = int(nromenu) + 1
                if nromenu in range(1, 14):
                    if nromenu == 1:
                        print("Fin del programa")  # Grupo 1
                    elif nromenu == 2:
                        edades.append(None)  # Grupo 2
                    elif nromenu == 3:
                        edades.append(None)  # Grupo 3
                    elif nromenu == 4:
                        print(edades)  # Grupo 4
                    elif nromenu == 5:
                        edades = edades  # Grupo 5
                    elif nromenu == 6:
                        edades = edades  # Grupo 6
                    elif nromenu == 7:
                        print(edades)  # Grupo 7
                    elif nromenu == 8:
                        print(edades)  # Grupo 8
                    elif nromenu == 9:
                        print(edades)  # Grupo 9
                    elif nromenu == 10:
                        edades = edades  # Grupo 10
                    elif nromenu == 11:
                        edades = edades  # Grupo 11
                    elif nromenu == 12:
                        edades = edades  # Grupo 12
                    elif nromenu == 13:
                        edades = edades  # Grupo 13
                    elif nromenu == 14:
                        edades = edades  # Grupo 14
                else:
                    print("El numero ingresado no esta dentro del rango")
            else:
                print("El valor ingresado no es un numero")
    except:
        print("Error MENU")


if __name__ == "__main__":
    menu()
