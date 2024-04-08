def edad_mayor(edad):
    return max(edad)

def sumatotal(lista):
    sumaEdad=0
    for edad in lista:
        sumaEdad=sumaEdad+edad
    return sumaEdad

def mostrar_edades(edades, prom):
    mayores = []
    for edad in edades:
        if edad > prom:
            mayores.append(edad)

    return mayores

def mostrar_lista(lista):
    for i in lista:
        print(i)

def ordenAscendente(edades):
    listaOrdenada = sorted(edades)
    return listaOrdenada

def menor_edad(lista):
    min = 130
    for i in range(len(lista)):
        if lista[i] < min:
            min = lista[i]
    return min

def mayor_a_promedio(edades,prom):
    mayores=[]
    for edad in edades:
        if edad > prom :
            mayores.append(edad)
    return mayores

def orden_desc(lista):
    lista_desc= sorted(lista,reverse=True)
    print(lista_desc)

def leeredades():
    lista= []
    with open("edades.txt", 'r') as archivo:
        for linea in archivo:
            edad = int(linea.strip())
            lista.append(edad)
    return lista

def cargar_edades():
    opcion = 1
    lista = []
    while opcion!=0 :
        edad = int (input("Ingrese edad o presione 0 para sali: "))
        if(edad==0):
            opcion=0
            break
        lista.append(edad)
    return lista

def promedio (SumaEdad, lista):
    cantidadEdades = len(lista)
    prom = SumaEdad / cantidadEdades
    return prom

def diferencia(edad,promedio):
    return edad-promedio

def escribir_edad_en_letras(edad):
    unidades = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
    diez_hasta_veinte = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve']
    decenas = ['veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
    edad_en_letras = ''
    try:
        edad = int(edad)
    except ValueError:
        print("❌Error. La edad dada no es valida. Asegure que sea un número entero")
        return
    match(len(str(edad))):
        case 1:
            edad_en_letras = unidades[edad - 1]
        case 2:
            edad_decena, edad_unidad = [edad // 10, edad % 10]
            if edad < 20:
                edad_en_letras = diez_hasta_veinte[edad_unidad]
            elif 30 > edad > 20:
                edad_en_letras = decenas[edad_decena - 2]
                edad_en_letras += f'i{unidades[edad_unidad - 1]}' if edad_unidad > 0 else ''
            else:
                edad_en_letras = decenas[edad_decena - 2]
                edad_en_letras += f' y {unidades[edad_unidad - 1]}' if edad_unidad > 0 else ''
        case _:
            print("❌ La edad seleccionada no es valida. Porfavor escoja una edad en el rango de 1 a 99")
            return
    print(f'La edad en letras es {edad_en_letras}')

if __name__ == "__main__":
    pass

