# Daniel Niño Muñoz
# parte 2

import pandas as pd

# Busqueda sequencial
def Secuencial(lista, elemento, longitud):
    # Se busca el elemento en linea de como esten ordenados los datos
    for i in range(longitud):
        if lista.loc[i]['twitter_name'] == elemento:
            print("Encontrado")
            registro = lista.loc[i]
            print(registro)
            return
    print("Usuario no se encuentra en la base de datos")
    pass


# Ordenamiento Seleccion
def Seleccion(lista, longitud):
    # Se ordena buscando la posicion del elemento mas grande
    n = longitud - 1
    # Se toma en cuenta la cantidad de elementos por ordenar
    while n > 0:
        p = 0
        for i in range(p + 1, n + 1):
            if lista.loc[i]['number_of_likes'] > lista.loc[p]['number_of_likes']:
                p = i
        lista.loc[p], lista.loc[n] = lista.loc[n].copy(), lista.loc[p].copy()
        n = n - 1
    print("Los 3 mejores tweets fueron: ")
    print(lista[['number_of_likes', 'text']].tail(3))
    pass


# main
def main():
    # menu para realizar las busquedas
    print("-----------------------------")
    print(" -- Tweets --")
    print("-----------------------------")
    print("1. Buscar 3 mejores")
    print("2. Buscar por usuario")
    print("3. Salir")
    # opcion es para elegir que camino tomar en caso de ser diferente a las opciones impresas en pantalla se vuelve a imprimir las opciones
    opcion = -1
    opcion = int(input())
    if opcion == 1:
        # importar los datos del archivo excel
        lista = pd.read_csv("dataPUJ-marzo.csv")
        lista = lista.drop("Unnamed: 0", axis=1)
        Seleccion(lista, len(lista))
        main()
    elif opcion == 2:
        lista = pd.read_csv("dataPUJ-marzo.csv")
        lista = lista.drop("Unnamed: 0", axis=1)
        Busqueda = str(input("Usuario que se desea buscar: "))
        Secuencial(lista, Busqueda, len(lista))
        main()
    elif opcion == 3:
        return
    else:
        main()
    return


if __name__ == "__main__":
    main()
