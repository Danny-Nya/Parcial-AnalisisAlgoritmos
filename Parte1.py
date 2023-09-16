# Daniel Niño Muñoz
# parte 1
import random
import time
import pandas as pd
import matplotlib.pyplot as plt


# funciones de Busqueda
# Busqueda sequencial
def Secuencial(lista, elemento, longitud):
    # Se busca el elemento en linea de como esten ordenados los datos
    for i in range(longitud):
        if lista[i] == elemento:
            print("Encontrado")
            registro = lista[i]
            print(registro)
            return
    print("No se encontro")
    pass


# Busqueda Binaria
def Binaria(lista, elemento):
    # Se busca el elemento en una lista ordenada
    lista = sorted(lista)
    low = 0
    high = len(lista) - 1
    mid = 0
    # Se selecciona la mitad mas cercana al dato
    while low <= high:
        mid = (high + low) // 2
        if lista[mid] < elemento:
            low = mid + 1
        elif lista[mid] > elemento:
            high = mid - 1
        else:
            print("Encontrado")
            registro = lista[mid]
            print(registro)
            return
    print("No se encontro")
    pass


# Busqueda de esquinas
def Esquinas(lista, elemento, longitud):
    i = 0
    f = longitud - 1
    # Se busca el elemento en linea de como esten ordenados los datos
    while i < f:
        # Se busca el elemento desde el inicio y el final, hasta que se crucen los valores
        if lista[i] == elemento:
            print("Encontrado")
            registro = lista[i]
            print(registro)
            return
        else:
            i += 1
        if lista[f] == elemento:
            print("Encontrado")
            registro = lista[f]
            print(registro)
            return
        else:
            f -= 1
    print("No se encontro")
    pass


# funciones de Ordenamiento
# Ordenamiento Bubble
def Bubble(lista, longitud):
    # Se intercambian los datos a medida que se recorre la lista
    for i in range(longitud - 1, 0, -1):
        for j in range(i):
            if (lista[j] > lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print("Ordenado")
    pass


# Ordenamiento Seleccion
def Seleccion(lista, longitud):
    # Se ordena buscando la posicion del elemento mas grande
    n = len(lista) - 1
    # Se toma en cuenta la cantidad de elementos por ordenar
    while n > 0:
        p = 0
        for i in range(p + 1, n + 1):
            if lista[i] > lista[p]:
                p = i
        lista[p], lista[n] = lista[n], lista[p]
        n = n - 1
    print("Ordenado")
    pass


# Ordenamiento Insercion
def Insercion(lista, longitud):
    # Se Ordena garantizando que a medida que se encuentran datos estos se organizan
    for indice in range(1, longitud):
        valorActual = lista[indice]
        posicion = indice
        while posicion > 0 and lista[posicion - 1] > valorActual:
            lista[posicion] = lista[posicion - 1]
            posicion = posicion - 1
        lista[posicion] = valorActual
    print("Ordenado")
    pass


# funcion para crear un arreglo de numeros aleatorios para las pruebas
def createArray(n):
    m = []
    for i in range(n):
        m.append(random.randint(1, 100))
    return m


# main
def main():
    # df = pd.read_csv('dataPUJ-marzo.csv')
    dfb = pd.DataFrame(columns=['Registros', 't_Binaria', 't_Sequencial', 't_Esquinas'])
    Registros = []
    t_Binaria = []
    t_Sequencial = []
    t_Esquinas = []
    dfo = pd.DataFrame(columns=['Registros', 't_Bubble', 't_Seleccion', 't_Insercion'])
    Registros = []
    t_Bubble = []
    t_Seleccion = []
    t_Insercion = []
    n = 1
    m = []
    # repertir con diferentes cantidades de datos asi se ve su desempeno a medida que los datos aumentan (para este caso 5 repeticiones multiplicanto los datos por 5 en cada ronda)
    for i in range(5):
        print("_______________________")
        print(i)
        n = n * 5
        # crear una lista aleatoria para la buaqueda binaria
        m = createArray(n)
        t0 = time.perf_counter()
        print("Binaria")
        Binaria(m, 101)
        t1 = time.perf_counter()
        t_Binaria.append(t1 - t0)
        m = []
        # crear una lista aleatoria para la buaqueda Secuencial
        m = createArray(n)
        t0 = time.perf_counter()
        print("Secuencial")
        Secuencial(m, 101, n)
        t1 = time.perf_counter()
        t_Sequencial.append(t1 - t0)
        m = []
        # crear una lista aleatoria para la buaqueda por esquinas
        m = createArray(n)
        t0 = time.perf_counter()
        print("Esquinas")
        Esquinas(m, 101, n)
        t1 = time.perf_counter()
        t_Esquinas.append(t1 - t0)
        Registros.append(n)
        m = []
        # crear una lista aleatoria para el ordenamiento de burbuja
        m = createArray(n)
        t0 = time.perf_counter()
        print("Burbuja")
        Bubble(m, n)
        t1 = time.perf_counter()
        t_Bubble.append(t1 - t0)
        m = []
        # crear una lista aleatoria para el ordenamiento de burbuja
        m = createArray(n)
        t0 = time.perf_counter()
        print("Seleccion")
        Seleccion(m, n)
        t1 = time.perf_counter()
        t_Seleccion.append(t1 - t0)
        m = []
        # crear una lista aleatoria para el ordenamiento de burbuja
        m = createArray(n)
        t0 = time.perf_counter()
        print("Insercion")
        Insercion(m, n)
        t1 = time.perf_counter()
        t_Insercion.append(t1 - t0)
        m = []
        # se crea una lista para cada caso asi no se migran los cambios de orden en las listas beneficiando el rendimiento de algunos casos
    # insertar los datos de la tabla de Busquedas
    dfb['Registros'] = Registros
    dfb['t_Binaria'] = t_Binaria
    dfb['t_Sequencial'] = t_Sequencial
    dfb['t_Esquinas'] = t_Esquinas
    print(dfb)
    # Graficar
    dfb.plot(x='Registros', y=['t_Binaria', 't_Sequencial', 't_Esquinas'])
    plt.grid()
    plt.show()
    # insertar los datos de la tabla de Ordenamientos
    dfo['Registros'] = Registros
    dfo['t_Bubble'] = t_Bubble
    dfo['t_Seleccion'] = t_Seleccion
    dfo['t_Insercion'] = t_Insercion
    print(dfo)
    # Graficar
    dfo.plot(x='Registros', y=['t_Bubble', 't_Seleccion', 't_Insercion'])
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
