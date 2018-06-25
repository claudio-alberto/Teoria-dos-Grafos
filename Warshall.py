def inicio():
    vert = input().split(", ")
    aresta = input().split(", ")
    dicio = {}
    adjacentes = []
    arestas = []
    for i in range(len(aresta)):
        separando = aresta[i].split("(")
        nome_arestas = separando[1].split(")")
        dicio[separando[0]] = nome_arestas[0]
        adjacentes.append(nome_arestas[0])
        arestas.append(separando[0])
    return (vert, dicio, adjacentes, arestas)

inicio1 = inicio()

def matriz_adjancecia(inicio1):
    matrizAdjacencia = []
    for i in inicio1[0]:
        linha = []
        for j in inicio1[0]:
            if(i + '-' + j in inicio1[2]):
                linha.append(1)
            else:
                linha.append(0)
        matrizAdjacencia.append(linha)
    return matrizAdjacencia

def warshall(matriz):
    matriz_alcance = matriz
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if(matriz_alcance[i][j] == 1):
                for k in range(len(matriz)):
                    matriz_alcance[j][k] = max(matriz_alcance[j][k], matriz_alcance[i][k])
    return matriz_alcance

x = matriz_adjancecia(inicio1)

def imprimeMatriz(matriz):
    print("Matriz de Warshall/Alcancabilidade")
    for i in matriz:
        for j in i:
            print(j, end=" ")
        print(" ")

imprimeMatriz(warshall(x))