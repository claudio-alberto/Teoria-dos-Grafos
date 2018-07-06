from grafos import Grafo

def nao_adjacentes(lista, vert):
    adjan = ''
    nao_adj = 'Nao Adjacentes: '
    aux = lista
    aux2 = []
    for i in vert:
        for j in lista:
            vert1 = j[0]
            vert2 = j[2]
            if((i != vert1 and i != vert2) and (str(i) + '-' + vert1) not in aux and (str(i) + '-' + vert2) not in aux):
                aux2.append(str(i) + '-' + vert1)
                aux2.append(str(i) + '-' + vert2)

    for i in aux2:
        nao_adj += i + ' '
    return nao_adj

def Adjancente_proprio(lista):
    for i in lista:
        compara = i[0] + '-' + i[0]
        if(compara == i):
            return "Laco: " + str(True)

    return "Laco: " + str(False)

def aresta_paralela(lista):
    for aresta in lista:
        compara = aresta[0] + '-' + aresta[2]
        compara2 = aresta[2] + '-' + aresta[0]
        if((compara in lista and compara2 in lista)):
            return "Possui aresta paralela: " + str(True)
    return "Possui aresta paralela: " + str(False)

def grau_vertice(lista, vert):
    vertice = input("Digite o vertice escolhido para saber o grau: ")
    grau = 0
    if(vertice not in vert):
        return str("Vertice não faz parte do grafo ")
    for i in lista:
        x = i
        if(x[0] == vertice or x[2] == vertice):
            grau += 1
    saida = ("O grau do vertice " + vertice +" eh "+ str(grau))
    return saida

def incidencia_de_arestas(arestas, lista, vert):
    vertice_incidente = input("Digite o vertice para saber as arestas indicentes: ")
    arestas_incidentes = 'Arestas indicentes: '
    if(vertice_incidente not in vert):
        return str("Vertice não faz parte do grafo ")
    for i in range(len(lista)):
        x = lista[i]
        if(x[0] == vertice_incidente or x[2] == vertice_incidente):
            arestas_incidentes += arestas[i] + ' '

    return arestas_incidentes

def grafo_completo(vert, lista):
    lista2 = []
    cont = 0
    for vertice in vert:
        for vertice2 in vert:
            x = vertice + '-' + vertice2
            x2 = vertice2 + '-' + vertice
            if(x in lista or x2 in lista):
                cont += 1

        if(cont == (len(vert)-1)):
            cont = 0
        else:
            return "Grafo completo: " + str(False)
    return "Grafo completo: " + str(True)

def inicio():
    print("Digite o grafo: ")
    vert = input().split(", ")
    aresta = input().split(", ")
    dicio = {}
    lista = []
    arestas = []

    for i in range(len(aresta)):
        separando = aresta[i].split("(")
        nome_arestas = separando[1].split(")")
        dicio[separando[0]] = nome_arestas[0]
        lista.append(nome_arestas[0])
        arestas.append(separando[0])
    return (vert, dicio, lista, arestas)

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

def menu(lista, vert, arestas, grafo, vertices):
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
        print('\n' + (nao_adjacentes(lista, vertices)) + '\n')
        print(grafo)
        menu(lista, vert, arestas, grafo, vertices)
    elif(opcao == 2):
        print('\n' + Adjancente_proprio(lista) + '\n')
        print(grafo)
        menu(lista, vert, arestas, grafo, vertices)
    elif(opcao == 3):
        print('\n' + aresta_paralela(lista) + '\n')
        print(grafo)
        menu(lista, vert, arestas, grafo, vertices)
    elif(opcao == 4):
        print('\n' + grau_vertice(lista, vert) + '\n')
        print(grafo)
        menu(lista, vert, arestas, grafo, vertices)
    elif(opcao == 5):
        print('\n' + incidencia_de_arestas(arestas, lista, vert) + '\n')
        print(grafo)
        menu(lista, vert, arestas, grafo, vertices)
    elif(opcao == 6):
        print('\n' + grafo_completo(vert, lista) + '\n')
        print(grafo)
        menu(lista, vert, arestas, grafo, vertices)
    elif(opcao == 7):
        inicio = input("Digite o vertice inicial para encontrar o caminho: ")
        fim = input('Digite o vertice final para encontrar o caminho: ')
        encontra_caminho(vert, lista, inicio, fim)
        print(grafo)
        menu(lista, vert, arestas, grafo, vertices)

    elif(opcao == 8):
        pass

# vert = [A, B, C]
# lista = ['A-B', 'B-C', 'C-A']
# a1(A-B), a2(B-C), a3(C-A)

while True:
    try:
        inicio1 = inicio()
        vertices = inicio1[0]
        dicio = inicio1[1]
        lista = inicio1[2]
        arestas = inicio1[3]
        grafo = Grafo(vertices, dicio)
        menu(lista, vertices, arestas, grafo, vertices)
    except:
        print("Arestas e/ou vértices inválidos!")
