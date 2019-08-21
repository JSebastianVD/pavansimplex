numero_varZ = (int(input("Digite el numero de variables en Z: ")))
numero_inec = (int(input("Digite el numero de inecuaciones: ")))
num_filas = numero_inec + 1
num_colum = numero_inec + numero_varZ + 2
matriz_1 = []
matriz_2 = []
num_pivoteZ = 0

print(str(num_filas) + " + " + str(num_colum))

for i in range(num_filas):
    matriz_1.append([])
    for j in range(num_colum):
        matriz_1[i].append(None)
for i in range(num_filas):
    matriz_2.append([])
    for j in range(num_colum):
        matriz_2[i].append(None)

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

for j in range(num_colum):
    if matriz_1[num_filas-1][j] < 0 and matriz_1[num_filas-1][j] < num_pivoteZ:
        num_pivoteZ = matriz_1[num_filas - 1][j]
        colum_pivote = j

for i in range(num_filas-1):
    if i == 0:
        num_menor = matriz_1[i][num_colum-1]/matriz_1[i][colum_pivote]
        fila_pivot = i
        elemento_pivote = matriz_1[i][colum_pivote]
    elif matriz_1[i][num_colum-1]/matriz_1[i][colum_pivote] < num_menor:
        num_menor = matriz_1[i][num_colum-1]/matriz_1[i][colum_pivote]
        fila_pivot = i
        elemento_pivote = matriz_1[i][colum_pivote]

for j in range(num_colum):
        matriz_2[fila_pivot][j] = matriz_1[fila_pivot][j] / elemento_pivote

for i in range(num_filas):
    for j in range(num_colum):
        if i != fila_pivot:
            matriz_2[i][j] = matriz_1[i][j]-(matriz_1[i][colum_pivote]*matriz_2[fila_pivot][j])

for i in range(num_filas):
    tot= ""
    for j in range(num_colum):
        tot = tot + str(matriz_2[i][j]) + "  "
    print(tot)