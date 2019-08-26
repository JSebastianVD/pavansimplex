numero_varZ = (int(input("Digite el numero de variables en Z: ")))
numero_inec = (int(input("Digite el numero de inecuaciones: ")))
num_filas = numero_inec + 1
num_colum = numero_inec + numero_varZ + 2
matriz_1 = []
matriz_2 = []
lista = []
respuestas = {}
global salidaaux
salidaaux = 1

def crear_matriz(matriz):
    for i in range(num_filas):
        matriz.append([])
        for j in range(num_colum):
            matriz[i].append(None)
    return matriz

def encontrar_columpiv(matriz):
    num_pivoteZ = 0
    global colum_pivote
    for j in range(num_colum):
        if matriz[num_filas - 1][j] < 0 and matriz[num_filas - 1][j] < num_pivoteZ:
            num_pivoteZ = matriz[num_filas - 1][j]
            colum_pivote = j

def encontrar_elemento_pivote(matriz):
    global fila_pivot
    num_menor = 1000
    for i in range(num_filas - 1):
        if matriz[i][colum_pivote]==0 or matriz[i][num_colum - 1] / matriz[i][colum_pivote] < 0:
            continue
        else:
            if i == 0:
                num_menor = matriz[i][num_colum - 1] / matriz[i][colum_pivote]
                fila_pivot = i
                elemento_pivote = matriz_1[i][colum_pivote]
            elif matriz[i][num_colum - 1] / matriz[i][colum_pivote] < num_menor:
                num_menor = matriz[i][num_colum - 1] / matriz[i][colum_pivote]
                fila_pivot = i
                elemento_pivote = matriz[i][colum_pivote]
    lista.append(fila_pivot)
    return elemento_pivote


def fila_entrante(matriznueva,matrizvieja):
    for j in range(num_colum):
        matriznueva[fila_pivot][j] = matrizvieja[fila_pivot][j] / elemento_pivote


def reorganizar_matriz(matriznueva):
    for i in range(num_filas):
        for j in range(num_colum):
            if i != fila_pivot:
                matriz_2[i][j] = matriz_1[i][j]-(matriz_1[i][colum_pivote]*matriz_2[fila_pivot][j])

def hay_negativos(matriznueva):
    negativo = None
    for j in range(num_colum-1):
        if matriznueva[num_filas-1][j] < 0:
            salidaaux = 1
            negativo = matriznueva[num_filas-1][j]
        elif negativo == None:
            salidaaux = 0
    return salidaaux

def imprimir_matriz(matriz):
    for i in range(num_filas):
        tot= ""
        for j in range(num_colum):
            tot = tot + str(matriz[i][j]) + "   "
        print(tot)
    print()

def limpiar_matriz(matriznueva, matrizvacia):
    for i in range(num_filas):
        for j in range(num_colum):
            matriznueva[i][j]=matrizvacia[i][j]

for i in range(num_filas):
    if i < num_filas-1:
        respuestas["S" + str(i+1)]= 0
    else:
        respuestas["Z"] = 0

matriz_1= crear_matriz(matriz_1)
matriz_2= crear_matriz(matriz_2)


print("PROGRAMA METODO SIMPLEX")
for i in range(num_filas):
    for j in range(num_colum):
        if j == 0 and i != num_filas - 1:
            matriz_1[i][j] = 0
        elif j == 0 and i == num_filas - 1:
            matriz_1[i][j] = 1
        elif 0 < j <= numero_varZ and i != num_filas - 1:
            matriz_1[i][j] = int(
                input("Digite el coeficiente de la variable " + str(j) + " de la ecuacion " + str(i + 1) + ": "))
        elif j == num_colum - 1 and i != num_filas - 1:
            matriz_1[i][j] = int(input("Digite el coeficiente al que esta igualado la ecuacion " + str(i + 1) + ": "))
        elif 0 < j <= numero_varZ and i == num_filas - 1:
            matriz_1[i][j] =int(input("Digite el coeficiente de la variable " + str(j) + " de la funcion Z: "))
            matriz_1[i][j] = matriz_1[i][j]*(-1)
        elif j == num_colum - 1 and i == num_filas - 1:
            matriz_1[i][j] = 0
        elif  numero_varZ < j < num_colum-1:
            if i== j - numero_varZ-1:
                matriz_1[i][j] = 1
            else:
                matriz_1[i][j] = 0




while salidaaux == 1:
    imprimir_matriz(matriz_1)
    encontrar_columpiv(matriz_1)
    elemento_pivote = encontrar_elemento_pivote(matriz_1)
    fila_entrante(matriz_2, matriz_1)
    reorganizar_matriz(matriz_2)
    salidaaux = hay_negativos(matriz_1)
    print(str(salidaaux))
    print(elemento_pivote)
    for i in range(num_filas):
        if i == fila_pivot:
            try:
                respuestas["X" + str(i + 1)] = respuestas.pop("S" + str(i + 1))
            except:
                respuestas["X" + str(i + 1)] = matriz_2[i][num_colum - 1]
        elif i == num_filas - 1:
            respuestas["Z"] = matriz_2[i][num_colum - 1]

    for i in range(num_filas):
        for j in range(len(lista)):
            if i == lista[j]:
                respuestas["X" + str(i + 1)] = matriz_2[i][num_colum - 1]

    for i in range(num_filas):
        for j in range(num_colum):
            matriz_1[i][j]=matriz_2[i][j]
    for i in range(num_filas):
        for j in range(num_colum):
            matriz_2[i][j]= None

print("Respuestas: ")
for key, value in respuestas.items():
    print(key + " = ", value)

