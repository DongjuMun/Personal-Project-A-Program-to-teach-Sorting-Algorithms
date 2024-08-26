#Descripcion general
"""
	La simulación de los algoritmos de ordenación 
    (Selección, Burbuja, Inserción, Mezcla, y Rápida.)
    Un algoritmo de ordenación es un conjunto de instrucciones que 
    toma un arreglo o lista como entrada y clasifica los elementos 
    en un orden específico. Las ordenaciones suelen ser numéricas 
    o alfabéticas (o de diccionario) y pueden ser ascendentes 
    (az, 0-9). Esos algoritmos son 
    esenciales para los que estudian ITC y la simulación de 
    los algoritmos les ayudarán mucho a entender.
"""


def creat_list(size): #la funcion para crear una lista
    list = []
    for i in range(size):
        num = int(input("Inserta un número a la lista: ")) 
        list.append(num)    
    print("\n")
    print("La lista es ", list)
    print("------------------------------------------------")
    return list

def change_stringstolist(cadena): #la funcion para cambiar unos strings a una lista
    lista = []
    for i in range(len(cadena)):
        lista.append(cadena[i]) #añadir los valores de los strings a la lista
    print("La cadena modificada a una lista es ", lista)
    print("------------------------------------------------")
    return lista, len(lista)


def selection(l, s): #la funcion para hacer el ordenamiento por seleccion 
    """
    El ordenamiento por selección mejora el ordenamiento burbuja 
    haciendo un sólo intercambio por cada pasada a través de la lista. 
    Para hacer esto, un ordenamiento por selección busca el valor 
    mayor a medida que hace una pasada y,
    después de completar la pasada, lo pone en la ubicación correcta.
    """
    min_index = 0 #el index del valor mas pequeño
    for i in range(s):
        min_index = i
        for j in range(i+1,s):
            if l[j] < l[min_index]:
                print(f"Se ha encontrado un número que es menos que list[{min_index}] = {min}. 
                        El número es list[{j}] = {l[j]} \n")
                min_index = j
        if min_index != i: #para imprimir las siguentes frases solo cuando hay cambio del min_index.
            print(f"El elemento de la lista que se va a cambiar es list[{i}] = {l[i]} \n")
            print(f"El elemento que tiene el valor más pequeño es list[{min_index}] = {l[min_index]} \n")
            l[i], l[min_index] = l[min_index], l[i]
            print("La lista modificada es: \n",l)
            print("------------------------------------------------")
    print("El resultado final es:\n", l)
    print("------------------------------------------------")

def bubble(l,s): #la funcion para hacer el ordenamiento de Burbuja. 
    """
    El ordenamiento de burbuja es un sencillo algoritmo de ordenamiento. 
    Funciona revisando cada elemento de la lista que va a ser ordenada con el siguiente, 
    intercambiándolos de posición si están en el orden equivocado.
    """
    for i in range(s-1,0,-1):
        for j in range(i):
            if l[j] > l[j+1]:
                print(f"El elemento list[{j+1}] = {l[j+1]} es menor que el elemento list[{j}] = {l[j]}")
                print("\n")
                l[j], l[j+1] = l[j+1], l[j]
                print("La lista modificada es: \n",l)
                print("------------------------------------------------")
    print("El resultado final es \n", l)
    print("------------------------------------------------")

def insertion(l,s): #la funcion para hacer el ordenamiento de inserción. 
    """
    El ordenamiento por inserción es una manera muy natural de ordenar para un ser humano, 
    y puede usarse fácilmente para ordenar un mazo de cartas numeradas en forma arbitraria.
    La idea de este algoritmo de ordenación consiste en ir insertando un elemento de la lista 
    ó un arreglo en la parte ordenada de la misma, asumiendo que el primer elemento es 
    la parte ordenada, el algoritmo ira comparando un elemento de la parte desordenada de 
    la lista con los elementos de la parte ordenada, insertando el elemento en la posición 
    correcta dentro de la parte ordenada, y así sucesivamente hasta obtener la lista ordenada.
    """
    for i in range(1,s): #empezando desde 1 hasta size-1
        for j in range(i,0,-1): #comparando los valores desde i hasta 0 (cuando j = 1 => j-1 = 0)
            if l[j-1] > l[j]:
                l[j-1], l[j] = l[j], l[j-1] #cambia los dos valores
        print("La lista modificada es: \n", l)
        print("------------------------------------------------")
    print()
    print("El resultado final es: \n", l)
    print("------------------------------------------------")      

def mergeSort(l):
    """
     El ordenamiento por mezcla es un algoritmo recursivo que divide continuamente 
     una lista por la mitad. Si la lista está vacía o tiene un solo ítem, se ordena 
     por definición (el caso base). Si la lista tiene más de un ítem, dividimos la 
     lista e invocamos recursivamente un ordenamiento por mezcla para ambas mitades. 
     Una vez que las dos mitades están ordenadas, se realiza la operación fundamental, 
     denominada mezcla. La mezcla es el proceso de tomar dos listas ordenadas más pequeñas 
     y combinarlas en una sola lista nueva y ordenada.
    """
    size = len(l) #el tamaño de la lista
    if size <= 1: return l #si el tamaño es menos o igual a 1, regresa la lista
    mid = len(l) // 2 #Dividir la lista en dos partes.
    print("la lista de left que va a ser el parametro de la funcion mergeSort() es ", l[:mid])
    print("la lista de right que va a ser el parametro de la funcion mergeSort() es ", l[mid:])
    print()
    left = mergeSort(l[:mid]) #asignar el resultado de la funcion mergeSort con la lista l[:mid] (funcion recursiva)
    right = mergeSort(l[mid:]) #asginar el resultado de la funcion mergeSort con la lista l[mid:] (funcion recursiva)
    print("La lista left es ", left)
    print("La lista right es ", right)
    print()
    merged = merge(left, right) #pegar las dos listas
    print("La lista merged es ", merged)
    print("------------------------------------------------")   

    return merged #regresar el resultado

def merge(list1, list2): #pegar las dos listas
	merged = [] # La lista para pegar los valores de las listas
	while len(list1) > 0 and len(list2) > 0:  #si hay valores en las listas
		if list1[0] <= list2[0]: #si el valor de la lista(left) es igual o menor al de la lista(right)
			merged.append(list1.pop(0)) #eliminar ese valor(lista1[0]) y pegarlo a la lista merged
		else:
			merged.append(list2.pop(0)) #si no, eliminar ese valor(lista2[0]) y pegarlo a la lista merged

	if len(list1) > 0: #si todavia hay valores en la lista aunque la otra ya no tenga valores
		merged += list1 #pegar todos los valores de esa lista a la lista merged
	if len(list2) > 0: #si todavia hay valores en la lista aunque la otra ya no tenga valores
		merged += list2 #pegar todos los valores de esa lista a la lista merged

	return merged #regresar el resultado 

def quick(l):
    """
    El ordenamiento rápido (tambien llamado ordonamiento de Hoare o quicksort en inglés) es 
    un algoritmo creado por el científico británico en computación Tony Hoare y basado en 
    la técnica de divide y vencerás. Esta es la técnica quizás la más eficiente y en ella 
    que en la mayoría de los casos da mejores resultados

    El algoritmo fundamental es el siguiente:
        1. Elegir un elemento de la lista de elementos a ordenar, al que llamaremos pivote.

        2. Resituar los demás elementos de la lista a cada lado del pivote, de manera que a 
        un lado queden todos los menores que él, y al otro los mayores. En este momento, 
        el pivote ocupa exactamente el lugar que le corresponderá en la lista ordenada.

        3. La lista queda separada en dos sublistas, una formada por los elementos a la izquierda 
        del pivote, y otra por los elementos a su derecha.

        4. Repetir este proceso de forma recursiva para cada sublista mientras éstas contengan 
        más de un elemento. Una vez terminado este proceso todos los elementos estarán ordenados.
    """
    if len(l) <= 1: #si el tamaño de lista es igual o menos a 1, solo regresa esa lista
        return l 
    pivot = l[len(l) // 2] #determinar el pivot
    print("El pivot es ", pivot)
    lesser_arr, equal_arr, greater_arr = [], [], [] 
    #la lista donde hay los valores que son menores que el pivot
    #/el pivot/la lista donde hay los valores que son mayores que el pivot 
    for num in l:
        if num < pivot:
            lesser_arr.append(num) #append los que sean menores que el pivot
            print("La lista de los valores que son menores que el pivot es ", num)
        elif num > pivot:
            greater_arr.append(num) #append los que sean mayores que el pivot
            print("La lista de los valores que son mayores que el pivot es ", num)
        else:
            equal_arr.append(num) #el pivot
    print("------------------------------------------------")  
    return quick(lesser_arr) + equal_arr + quick(greater_arr) 
    #regresa las listas pero hay que llamar la funcion quick() de nuevo (funcion recursiva)

def menu_main():
    print()
    print("1. Ordenamiento por Selección")
    print("2. Ordenamiento de Burbuja")
    print("3. Ordenamiento de inserción")
    print("4. Ordenamiento por mezcla")
    print("5. Ordenamiento rápdio")
    print("6. Salir")

def menu_stringsorlistofnumbers():
    print("1. lista de numeros")
    print("2. Strings")

def main():
    file = open("explicacion.txt", 'r') #abrir un archivo de texto para explicar el programa
    print(file.read())
    continua = True
    while continua:
        menu_main()
        option = int(input("Selecciona una opcion: "))
        if option == 1:
            print("Has seleccionado el Ordenamiento por Selección.")
            print("------------------------------------------------")
            menu_stringsorlistofnumbers()
            option_data = int(input("Selecciona una opcion: "))
            if option_data == 1:
                size = int(input("Dame el tamaño de la lista: "))
                if size > 0:
                    list = creat_list(size)
                    selection(list, size)
                else:
                    print("El tamaño debe ser mayor que 0.")
            elif option_data == 2:
                strings = str(input("Dame una cadena en que las caracteres no sean mayusculas: "))
                list, size = change_stringstolist(strings)
                if size > 0:
                    selection(list, size)
                else:
                    print("El tamaño debe ser mayor que 0.")
            else:
                print("Opcion invalida.")

        elif option == 2:
            print("Has seleccionado el Ordenamiento de burbuja.")
            print("------------------------------------------------")
            menu_stringsorlistofnumbers()
            option_data = int(input("Selecciona una opcion: "))
            if option_data == 1:
                size = int(input("Dame el tamaño de la lista: "))
                if size > 0:
                    list = creat_list(size)
                    bubble(list, size)
                else:
                    print("El tamaño debe ser mayor que 0.")
            elif option_data == 2:
                strings = str(input("Dame una cadena en que las caracteres no sean mayusculas: "))
                list, size = change_stringstolist(strings)
                if size > 0:
                    bubble(list, size)
                else:
                    print("El tamaño debe ser mayor que 0.")
            else:
                print("Opcion invalida.")

        elif option == 3:
            print("Has seleccionado el Ordenamiento de inserción.")
            print("------------------------------------------------")
            menu_stringsorlistofnumbers()
            option_data = int(input("Selecciona una opcion: "))
            if option_data == 1:
                size = int(input("Dame el tamaño de la lista: "))
                if size > 0:
                    list = creat_list(size)
                    insertion(list, size)
                else:
                    print("El tamaño debe ser mayor que 0.")
            elif option_data == 2:
                strings = str(input("Dame una cadena en que las caracteres no sean mayusculas: "))
                list, size = change_stringstolist(strings)
                if size > 0:
                    insertion(list, size)
                else:
                    print("El tamaño debe ser mayor que 0.")
            else:
                print("Opcion invalida.")

        elif option == 4:
            print("Has seleccionado el Ordenamiento por mezcla.")
            print("------------------------------------------------")
            menu_stringsorlistofnumbers()
            option_data = int(input("Selecciona una opcion: "))
            if option_data == 1:
                size = int(input("Dame el tamaño de la lista: "))
                if size > 0:
                    list = creat_list(size)
                    list = mergeSort(list)
                    print("El resultado es ", list)
                    print("------------------------------------------------")
                else:
                    print("El tamaño debe ser mayor que 0.")
            elif option_data == 2:
                strings = str(input("Dame una cadena en que las caracteres no sean mayusculas: "))
                list, size = change_stringstolist(strings)
                if size > 0:
                    list = mergeSort(list)
                    print("El resultado es ", list)
                    print("------------------------------------------------")
                else:
                    print("El tamaño debe ser mayor que 0.")
            else:
                print("Opcion invalida.")

        elif option == 5:
            print("Has seleccionado el Ordenamiento rápido.")
            print("------------------------------------------------")
            menu_stringsorlistofnumbers()
            option_data = int(input("Selecciona una opcion: "))
            if option_data == 1:
                size = int(input("Dame el tamaño de la lista: "))
                if size > 0:
                    list = creat_list(size)
                    list = quick(list)
                    print("El resultado es ", list)
                    print("------------------------------------------------")
                else:
                    print("El tamaño debe ser mayor que 0.")
            elif option_data == 2:
                strings = str(input("Dame una cadena en que las caracteres no sean mayusculas: "))
                list, size = change_stringstolist(strings)
                if size > 0:
                    list = quick(list)
                    print("El resultado es ", list)
                    print("------------------------------------------------")
                else:
                    print("El tamaño debe ser mayor que 0.")
            else:
                print("Opcion invalida.")

        elif option == 6:
            print("Adios")
            continua = False

        else:
            print("Opcion invalida.")
    file.close()

main()     

"""
<Caso de prueba>

0. explicacion.txt

    <La simulacion de los algoritmos de ordenacion>
    (Seleccion, Burbuja, Insercion, Mezcla, y Rapida.)
    Un algoritmo de ordenacion es un conjunto de instrucciones que toma un arreglo o 
    lista como entrada y clasifica los elementos en un orden especifico. Las ordenaciones 
    suelen ser numericas o alfabeticas (o de diccionario) y pueden ser ascendentes (az, 0-9). 
    Esos algoritmos son esenciales para los que estudian ITC y la simulacion de los algoritmos 
    les ayudaran mucho a entender.

1. Ordenamiento por Selección - Lista de numeros

    1. Ordenamiento por Selección
    2. Ordenamiento de Burbuja
    3. Ordenamiento de inserción
    4. Ordenamiento por mezcla
    5. Ordenamiento rápdio
    6. Salir
    Selecciona una opcion: 1
    Has seleccionado el Ordenamiento por Selección.
    ------------------------------------------------
    1. lista de numeros
    2. Strings
    Selecciona una opcion: 1
    Dame el tamaño de la lista: 5
    Inserta un número a la lista: 3
    Inserta un número a la lista: 1
    Inserta un número a la lista: 4
    Inserta un número a la lista: 2
    Inserta un número a la lista: 5


    La lista es  [3, 1, 4, 2, 5]
    ------------------------------------------------
    Se ha encontrado un número que es menos que list[0] = <built-in function min>. El número es list[1] = 1        

    El elemento de la lista que se va a cambiar es list[0] = 3

    El elemento que tiene el valor más pequeño es list[1] = 1

    La lista modificada es:
    [1, 3, 4, 2, 5]
    ------------------------------------------------
    Se ha encontrado un número que es menos que list[1] = <built-in function min>. El número es list[3] = 2        

    El elemento de la lista que se va a cambiar es list[1] = 3

    El elemento que tiene el valor más pequeño es list[3] = 2

    La lista modificada es:
    [1, 2, 4, 3, 5]
    ------------------------------------------------
    Se ha encontrado un número que es menos que list[2] = <built-in function min>. El número es list[3] = 3        

    El elemento de la lista que se va a cambiar es list[2] = 4

    El elemento que tiene el valor más pequeño es list[3] = 3

    La lista modificada es:
    [1, 2, 3, 4, 5]
    ------------------------------------------------
    El resultado final es:
    [1, 2, 3, 4, 5]
    ------------------------------------------------

1. Ordenamiento por Selección -  Strings
     
    1. Ordenamiento por Selección
    2. Ordenamiento de Burbuja
    3. Ordenamiento de inserción
    4. Ordenamiento por mezcla
    5. Ordenamiento rápdio
    6. Salir
    Selecciona una opcion: 1
    Has seleccionado el Ordenamiento por Selección.
    ------------------------------------------------
    1. lista de numeros
    2. Strings
    Selecciona una opcion: 2
    Dame una cadena en que las caracteres no sean mayusculas: ceadb
    La cadena modificada a una lista es  ['c', 'e', 'a', 'd', 'b']
    ------------------------------------------------
    Se ha encontrado un número que es menos que list[0] = <built-in function min>. El número es list[2] = a        

    El elemento de la lista que se va a cambiar es list[0] = c

    El elemento que tiene el valor más pequeño es list[2] = a

    La lista modificada es:
    ['a', 'e', 'c', 'd', 'b']
    ------------------------------------------------
    Se ha encontrado un número que es menos que list[1] = <built-in function min>. El número es list[2] = c        

    Se ha encontrado un número que es menos que list[2] = <built-in function min>. El número es list[4] = b        

    El elemento de la lista que se va a cambiar es list[1] = e

    El elemento que tiene el valor más pequeño es list[4] = b

    La lista modificada es:
    ['a', 'b', 'c', 'd', 'e']
    ------------------------------------------------
    El resultado final es:
    ['a', 'b', 'c', 'd', 'e']
    ------------------------------------------------

2. Ordenamiento de Burbuja - lista de numeros

    1. Ordenamiento por Selección
    2. Ordenamiento de Burbuja
    3. Ordenamiento de inserción
    4. Ordenamiento por mezcla
    5. Ordenamiento rápdio
    6. Salir
    Selecciona una opcion: 2
    Has seleccionado el Ordenamiento de burbuja.
    ------------------------------------------------
    1. lista de numeros
    2. Strings
    Selecciona una opcion: 1
    Dame el tamaño de la lista: 5
    Inserta un número a la lista: 2
    Inserta un número a la lista: 4
    Inserta un número a la lista: 1
    Inserta un número a la lista: 3
    Inserta un número a la lista: 5


    La lista es  [2, 4, 1, 3, 5]
    ------------------------------------------------
    El elemento list[2] = 1 es menor que el elemento list[1] = 4


    La lista modificada es:
    [2, 1, 4, 3, 5]
    ------------------------------------------------
    El elemento list[3] = 3 es menor que el elemento list[2] = 4


    La lista modificada es:
    [2, 1, 3, 4, 5]
    ------------------------------------------------
    El elemento list[1] = 1 es menor que el elemento list[0] = 2


    La lista modificada es:
    [1, 2, 3, 4, 5]
    ------------------------------------------------
    El resultado final es
    [1, 2, 3, 4, 5]
    ------------------------------------------------

2. Ordenamiento de Burbuja - Strings

    1. Ordenamiento por Selección
    2. Ordenamiento de Burbuja
    3. Ordenamiento de inserción
    4. Ordenamiento por mezcla
    5. Ordenamiento rápdio
    6. Salir
    Selecciona una opcion: 2
    Has seleccionado el Ordenamiento de burbuja.
    ------------------------------------------------
    1. lista de numeros
    2. Strings
    Selecciona una opcion: 2
    Dame una cadena en que las caracteres no sean mayusculas: adebc
    La cadena modificada a una lista es  ['a', 'd', 'e', 'b', 'c']
    ------------------------------------------------
    El elemento list[3] = b es menor que el elemento list[2] = e


    La lista modificada es:
    ['a', 'd', 'b', 'e', 'c']
    ------------------------------------------------
    El elemento list[4] = c es menor que el elemento list[3] = e


    La lista modificada es:
    ['a', 'd', 'b', 'c', 'e']
    ------------------------------------------------
    El elemento list[2] = b es menor que el elemento list[1] = d


    La lista modificada es:
    ['a', 'b', 'd', 'c', 'e']
    ------------------------------------------------
    El elemento list[3] = c es menor que el elemento list[2] = d


    La lista modificada es:
    ['a', 'b', 'c', 'd', 'e']
    ------------------------------------------------
    El resultado final es
    ['a', 'b', 'c', 'd', 'e']
    ------------------------------------------------

3. Ordenamiento de inserción - lista de numeros

    1. Ordenamiento por Selección
    2. Ordenamiento de Burbuja
    3. Ordenamiento de inserción
    4. Salir
    Selecciona una opcion: 3
        Has seleccionado el Ordenamiento de inserción.
        ------------------------------------------------
        1. lista de numeros
        2. Strings
    Selecciona una opcion: 1
        Dame el tamaño de la lista: 5
        Inserta un número a la lista: 3
        Inserta un número a la lista: 4
        Inserta un número a la lista: 1
        Inserta un número a la lista: 5
        Inserta un número a la lista: 2


        La lista es  [3, 4, 1, 5, 2]
        ------------------------------------------------
        La lista modificada es:
        [3, 4, 1, 5, 2]
        ------------------------------------------------
        La lista modificada es:
        [1, 3, 4, 5, 2]
        ------------------------------------------------
        La lista modificada es:
        [1, 3, 4, 5, 2]
        ------------------------------------------------
        La lista modificada es:
        [1, 2, 3, 4, 5]
        ------------------------------------------------

        El resultado final es:
        [1, 2, 3, 4, 5]
        ------------------------------------------------

3. Ordenamiento de inserción - strings

    1. Ordenamiento por Selección
    2. Ordenamiento de Burbuja
    3. Ordenamiento de inserción
    4. Ordenamiento por mezcla
    5. Ordenamiento rápdio
    6. Salir
    Selecciona una opcion: 3
    Has seleccionado el Ordenamiento de inserción.
    ------------------------------------------------
    1. lista de numeros
    2. Strings
    Selecciona una opcion: 2
    Dame una cadena en que las caracteres no sean mayusculas: eacbd
    La cadena modificada a una lista es  ['e', 'a', 'c', 'b', 'd']
    ------------------------------------------------
    La lista modificada es:
    ['a', 'e', 'c', 'b', 'd']
    ------------------------------------------------
    La lista modificada es:
    ['a', 'c', 'e', 'b', 'd']
    ------------------------------------------------
    La lista modificada es:
    ['a', 'b', 'c', 'e', 'd']
    ------------------------------------------------
    La lista modificada es:
    ['a', 'b', 'c', 'd', 'e']
    ------------------------------------------------

    El resultado final es:
    ['a', 'b', 'c', 'd', 'e']
    ------------------------------------------------

4. Ordenamiento por mezcla - lista de numeros

    1. Ordenamiento por Selección
    2. Ordenamiento de Burbuja
    3. Ordenamiento de inserción
    4. Ordenamiento por mezcla
    5. Ordenamiento rápdio
    6. Salir
    Selecciona una opcion: 4
    Has seleccionado el Ordenamiento por mezcla.
    ------------------------------------------------
    1. lista de numeros
    2. Strings
    Selecciona una opcion: 1
    Dame el tamaño de la lista: 5
    Inserta un número a la lista: 3
    Inserta un número a la lista: 5
    Inserta un número a la lista: 1
    Inserta un número a la lista: 4
    Inserta un número a la lista: 2


    La lista es  [3, 5, 1, 4, 2]
    ------------------------------------------------
    la lista de left que va a ser el parametro de la funcion mergeSort() es  [3, 5]
    la lista de right que va a ser el parametro de la funcion mergeSort() es  [1, 4, 2]

    la lista de left que va a ser el parametro de la funcion mergeSort() es  [3]
    la lista de right que va a ser el parametro de la funcion mergeSort() es  [5]

    La lista left es  [3]
    La lista right es  [5]

    La lista merged es  [3, 5]
    ------------------------------------------------
    la lista de left que va a ser el parametro de la funcion mergeSort() es  [1]
    la lista de right que va a ser el parametro de la funcion mergeSort() es  [4, 2]

    la lista de left que va a ser el parametro de la funcion mergeSort() es  [4]
    la lista de right que va a ser el parametro de la funcion mergeSort() es  [2]

    La lista left es  [4]
    La lista right es  [2]

    La lista merged es  [2, 4]
    ------------------------------------------------
    La lista left es  [1]
    La lista right es  [2, 4]

    La lista merged es  [1, 2, 4]
    ------------------------------------------------
    La lista left es  [3, 5]
    La lista right es  [1, 2, 4]

    La lista merged es  [1, 2, 3, 4, 5]
    ------------------------------------------------
    El resultado es  [1, 2, 3, 4, 5]
    ------------------------------------------------

4. Ordenamiento por mezcla - lista de numeros
    
    1. Ordenamiento por Selección
    2. Ordenamiento de Burbuja
    3. Ordenamiento de inserción
    4. Ordenamiento por mezcla
    5. Ordenamiento rápdio
    6. Salir
    Selecciona una opcion: 4
    Has seleccionado el Ordenamiento por mezcla.
    ------------------------------------------------
    1. lista de numeros
    2. Strings
    Selecciona una opcion: 2
    Dame una cadena en que las caracteres no sean mayusculas: eacbd
    La cadena modificada a una lista es  ['e', 'a', 'c', 'b', 'd']
    ------------------------------------------------
    la lista de left que va a ser el parametro de la funcion mergeSort() es  ['e', 'a']
    la lista de right que va a ser el parametro de la funcion mergeSort() es  ['c', 'b', 'd']

    la lista de left que va a ser el parametro de la funcion mergeSort() es  ['e']
    la lista de right que va a ser el parametro de la funcion mergeSort() es  ['a']

    La lista left es  ['e']
    La lista right es  ['a']

    La lista merged es  ['a', 'e']
    ------------------------------------------------
    la lista de left que va a ser el parametro de la funcion mergeSort() es  ['c']
    la lista de right que va a ser el parametro de la funcion mergeSort() es  ['b', 'd']

    la lista de left que va a ser el parametro de la funcion mergeSort() es  ['b']
    la lista de right que va a ser el parametro de la funcion mergeSort() es  ['d']

    La lista left es  ['b']
    La lista right es  ['d']

    La lista merged es  ['b', 'd']
    ------------------------------------------------
    La lista left es  ['c']
    La lista right es  ['b', 'd']

    La lista merged es  ['b', 'c', 'd']
    ------------------------------------------------
    La lista left es  ['a', 'e']
    La lista right es  ['b', 'c', 'd']

    La lista merged es  ['a', 'b', 'c', 'd', 'e']
    ------------------------------------------------
    El resultado es  ['a', 'b', 'c', 'd', 'e']
    ------------------------------------------------

5. Ordenamiento rápdio - lista de numeros

    1. Ordenamiento por Selección
    2. Ordenamiento de Burbuja
    3. Ordenamiento de inserción
    4. Ordenamiento por mezcla
    5. Ordenamiento rápdio
    6. Salir
    Selecciona una opcion: 5
    Has seleccionado el Ordenamiento rápido.
    ------------------------------------------------
    1. lista de numeros
    2. Strings
    Selecciona una opcion: 1
    Dame el tamaño de la lista: 5
    Inserta un número a la lista: 3
    Inserta un número a la lista: 1
    Inserta un número a la lista: 4
    Inserta un número a la lista: 2
    Inserta un número a la lista: 5


    La lista es  [3, 1, 4, 2, 5]
    ------------------------------------------------
    El pivot es  4
    La lista de los valores que son menores que el pivot es  3
    La lista de los valores que son menores que el pivot es  1
    La lista de los valores que son menores que el pivot es  2
    La lista de los valores que son mayores que el pivot es  5
    ------------------------------------------------
    El pivot es  1
    La lista de los valores que son mayores que el pivot es  3
    La lista de los valores que son mayores que el pivot es  2
    ------------------------------------------------
    El pivot es  2
    La lista de los valores que son mayores que el pivot es  3
    ------------------------------------------------
    El resultado es  [1, 2, 3, 4, 5]
    ------------------------------------------------

5. Ordenamiento rápdio - Strings

    1. Ordenamiento por Selección
    2. Ordenamiento de Burbuja
    3. Ordenamiento de inserción
    4. Ordenamiento por mezcla
    5. Ordenamiento rápdio
    6. Salir
    Selecciona una opcion: 5
    Has seleccionado el Ordenamiento rápido.
    ------------------------------------------------
    1. lista de numeros
    2. Strings
    Selecciona una opcion: 2
    Dame una cadena en que las caracteres no sean mayusculas: eabcd
    La cadena modificada a una lista es  ['e', 'a', 'b', 'c', 'd']
    ------------------------------------------------
    El pivot es  b
    La lista de los valores que son mayores que el pivot es  e
    La lista de los valores que son menores que el pivot es  a
    La lista de los valores que son mayores que el pivot es  c
    La lista de los valores que son mayores que el pivot es  d
    ------------------------------------------------
    El pivot es  c
    La lista de los valores que son mayores que el pivot es  e
    La lista de los valores que son mayores que el pivot es  d
    ------------------------------------------------
    El pivot es  d
    La lista de los valores que son mayores que el pivot es  e
    ------------------------------------------------
    El resultado es  ['a', 'b', 'c', 'd', 'e']
    ------------------------------------------------

6. Salir
    input: 6
        Adios
        (El programa termina)
    
7. Opcion invalida
    input: 9
        Opcion invalida.
"""