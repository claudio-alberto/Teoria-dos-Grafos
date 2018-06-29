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

def conexo(matriz_alcance):
    for i in range(len(matriz_alcance)):
        for j in range(len(matriz_alcance[i])):
            if(matriz_alcance[i][j] != 1):
                return "O grafo é conexo: " + str(False)
    return "O grado é conexo: " + str(True)

def constroi_matriz(inicio1):
    matriz = []
    for i in inicio1[0]:
        linha = []
        for j in inicio1[0]:
            if(i + '-' + j in inicio1[2]):
                linha.append(1)
            else:
                linha.append(0)
        matriz.append(linha)
    return matriz

def matriz_nao_direcionada(matriz):
    matriz_nao_direcional = matriz

    for i in range(len(matriz_nao_direcional)):
        for j in range(len(matriz_nao_direcional)):
            if(matriz_nao_direcional[i][j] == 1):
                matriz_nao_direcional[j][i] = 1
    return matriz_nao_direcional

def imprime_matriz(matriz):
    print("***Matriz***")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print(" ")

matriz1 = constroi_matriz(inicio1)
matriz1 = matriz_nao_direcionada(matriz1)

def findpath(graph, inicio):
    tam_grafo = len(graph)
    numofadj = list()
    valor_letras = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F",
                    8: "G", 9: "H", 10: "I", 11: "J",  12: "K", 13: "L",
                    14: "M", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S",
                    20: "T", 21: "U", 22: "V", 23: "X", 24: "Y", 25: "Z"}

    """ Descobrir o número de arestas de cada vértice"""
    pares = []
    impares = []
    vertices = inicio[0]
    arestas = inicio[2]

    for i in range(len(vertices)):
        cont = 0
        for j in range(len(arestas)):
            x = arestas[j]
            if(vertices[i] == x[0] or vertices[i] == x[2]):
                cont += 1
        if cont%2 == 0:
            pares.append(vertices[i])
        else:
            impares.append(vertices[i])

    if len(impares) > 2:
        return "Grafo sem caminho euleriano"



    for i in range(tam_grafo):
        numofadj.append(sum(graph[i]))
        print(sum(graph[i]))
    print(numofadj)

    """Descobrir quantos vértices são ímpares"""

    inicio = 0
    for i in range(tam_grafo - 1, -1, -1):
        if (numofadj[i] % 2 == 1):
            inicio = i

    """Se número de vértices com número ímpar de arestas é maior que dois retorna "Sem Caminho Euleriano"."""

    """Se houver um caminho, encontre o caminho
        Inicializar pilha e caminho vazios
        pegue a corrente de partida como discutido"""

    pilha = list()
    caminho = list()
    atual = inicio

    """O loop será executado até que haja um elemento na pilha
     ou borda atual tem algum vizinho. """

    while (pilha != [] or sum(graph[atual]) != 0):

        """Se o elemento atual nao tiver nenhum vizinho, 
        adicione ao caminho e apague da pilha
        Definir novo atual para apagar elemento """

        if (sum(graph[atual]) == 0):
            caminho.append(atual + 1)
            atual = pilha.pop(-1)

        # If the current vertex has at least one
        # neighbour add the current vertex to stack,
        # remove the edge between them and set the
        # current to its neighbour.
        else:
            for i in range(tam_grafo):
                if graph[atual][i] == 1:
                    pilha.append(atual)
                    graph[atual][i] = 0
                    graph[i][atual] = 0
                    atual = i
                    break
    # print the path
    for ele in caminho:
        print(valor_letras[ele], "-> ", end='')
    print(valor_letras[atual + 1])

findpath(matriz1, inicio1)

def matriz_nao_direcionada(matriz):
    matriz_nao_direcional = matriz

    for i in range(len(matriz_nao_direcional)):
        for j in range(len(matriz_nao_direcional)):
            if(matriz_nao_direcional[i][j] == 1):
                matriz_nao_direcional[j][i] = 1
    return matriz_nao_direcional

def warshall(matriz):
    matriz_alcance = matriz

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if(matriz_alcance[j][i] == 1):

                for k in range(len(matriz)):
                    matriz_alcance[j][k] = max(matriz_alcance[j][k], matriz_alcance[i][k])

    return matriz_alcance

def existe_caminho_euleriano(matriz):
    """Descobre se o grafo possui caminho euleriano"""

    if conexo(matriz) is False:
        print("Não existe caminho eureliano")
    else:
        total = 0
        i = 0
        while (total <= 2) and (i < len(matriz)):
            grau = 0
            for j in range(len(matriz)):
                grau += matriz[i][j]
                grau += matriz[j][i]
            if grau % 2 == 1:
                total += 1
            i += 1
        if total > 2:
            print("Não existe caminho eureliano")
        else:
            print("Existe caminho eureliano")


