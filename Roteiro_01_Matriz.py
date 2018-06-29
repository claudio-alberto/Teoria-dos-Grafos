from grafos import Grafo
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

def nao_adjacente(matriz, vertices):
    nao_adj = 'Não Adjacentes: '
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(matriz[i][j] == 0):
                nao_adj += vertices[i] + '-' + vertices[j] + ', '
    return nao_adj

def laco(matriz, vertices):
    laco = 'Laço(s): '
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(vertices[i] == vertices[j] and matriz[i][j] == 1):
                laco += vertices[i] + '-' + vertices[j] + ' '
    return laco

def aresta_paralela(matriz, vertices):
    paralela = 'Paralela: '
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(matriz[i][j] == 1):
                paralela += vertices[i] + '-' + vertices[j] + ', '
                paralela += vertices[j] + '-' + vertices[i] + ', '
    return paralela

def grau_vertice(matriz, vertices):
    vertice = input("Digite o vertice que deseja saber o grau: ")
    posicao = vertices.index(vertice)
    grau = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(matriz[i][j] == 1 and (i == posicao or j == posicao)):
                grau += 1
    return  'O grau do vertice é: ' + str(grau)

def incidencia_de_arestas(matriz, vertices, dicio):
    nome_arestas = 'Arestas incidentess: '
    vertice = input('Vertice a encontrar arestas: ')
    posicao = vertices.index(vertice)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            x = vertices[i] + '-' + vertices[j]
            adjancencias = list(dicio.values())
            arestas = list(dicio.keys())
            if(matriz[i][j] == 1 and  x in adjancencias and (x[0] == vertices[posicao] or x[2] == vertices[posicao])):
                pos = adjancencias.index(x)
                nome_arestas += arestas[pos] + ' '
    return nome_arestas

def encontra_caminho(vertices, adjacencia, inicio2, final):
    grafinho = {}

    for i in vertices:
        if(i not in grafinho):
            lis = []
            grafinho[i] = lis
            for j in adjacencia:
                if(i == j[0] and j[2] not in lis):
                    lis.append(j[2])
                elif(i == j[2] and j[0] not in lis):
                    lis.append(j[0])


    def gerar_caminhos(grafo, inicio, final):  # Mostra todos os caminhos no grafo `grafo` iniciados em "inicio" e que terminam no vértice 'final'
        if inicio[-1] == final:                # Se o caminho de fato atingiu o vértice final, para.
            yield inicio
            return
        for vizin in grafinho[inicio[-1]]: # Procuramos todos os vértices para os quais podemos avançar

            if vizin in inicio:    # Não podemos visitar um vértice que já está no caminho.
                continue
            for caminho_maior in gerar_caminhos(grafo, inicio + [vizin], final):
                yield caminho_maior

    for caminho in gerar_caminhos(grafinho, [inicio2], final):
        print (str('Caminhos: '), caminho)

def menu(lista, vert, arestas, grafo, vertices, dicio):
    print("1 - Encontre todos os pares de vértices não adjacentes")
    print("2 - Há algum vértice adjacente a ele mesmo?")
    print("3 - Há arestas paralelas?")
    print("4 - Qual o grau do vértice?")
    print("5 - Quais arestas incidem sobre o vértice?")
    print("6 - Esse grafo é completo?")
    print("7 - Encontrar Caminho (Desafio)")
    print("8 - Mudar Grafo")

    opcao = int(input("Digite a opção desejada: "))

    if(opcao == 1):
        print('\n' + (nao_adjacente(matriz, vertices)) + '\n')
        print(grafo)
        menu(lista, vert, arestas, grafo, vertices, dicio)
    elif(opcao == 2):
        print('\n' + laco(matriz, vertices) + '\n')
        print(grafo)
        menu(lista, vert, arestas, grafo, vertices, dicio)
    elif(opcao == 3):
        print('\n' + aresta_paralela(matriz, vertices) + '\n')
        print(grafo)
        menu(lista, vert, arestas, grafo, vertices, dicio)
    elif(opcao == 4):
        print('\n' + grau_vertice(matriz, vertices) + '\n')
        print(grafo)
        menu(lista, vert, arestas, grafo, vertices, dicio)
    elif(opcao == 5):
        print('\n' + incidencia_de_arestas(matriz, vertices, dicio) + '\n')
        print(grafo)
        menu(lista, vert, arestas, grafo, vertices, dicio)
    elif(opcao == 6):
        #print('\n' + grafo_completo(vert, lista) + '\n')
        print(grafo)
        menu(lista, vert, arestas, grafo, vertices, dicio)
    elif(opcao == 7):
        inicio = input("Digite o vertice inicial para encontrar o caminho: ")
        fim = input('Digite o vertice final para encontrar o caminho: ')
        encontra_caminho(vert, lista, inicio, fim)
        print(grafo)
        menu(lista, vert, arestas, grafo, vertices, dicio)


while True:
    try:
        inicio1 = inicio()
        matriz = []

        for i in inicio1[0]:
            linha = []
            for j in inicio1[0]:
                if(i + '-' + j in inicio1[2]):
                    linha.append(1)
                else:
                    linha.append(0)
            matriz.append(linha)
        print(inicio1)

        vertices = inicio1[0]
        dicio = inicio1[1]
        lista = inicio1[2]
        arestas = inicio1[3]
        grafo = Grafo(vertices, dicio)
        menu(lista, vertices, arestas, grafo, vertices, dicio)
    except:
        print("Arestas e/ou vértices inválidos!")

