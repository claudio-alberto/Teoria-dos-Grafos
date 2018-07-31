# grafo = {No_01 : { Vizinho1 : Peso_da_aresta, Vizinho2 : Peso_da_aresta },No_02 : { Vizinho1 : Peso_da_aresta}

grafo = {"A": {"BR": 20, "C": 20},
         "BR": {"D": 30, "E": 40},
         "C": {"E": 20},
         "D": {"F": 60},
         "E": {"F": 70},
         "F": {}}
grafo1 = { "A":{"B": 10, "C": 10},
           "B":{"F": 30, "E": 10},
           "C":{"D": 20, "F": 15},
           "D":{"HR": 40, "K": 30},
           "E":{"G": 20, "P": 30},
           "P":{"J": 40},
           "F":{"G": 15, "HR": 20},
           "G":{"I": 40, "P": 15},
           "HR":{"K": 30, "I": 15, "L": 10},
           "I":{"J": 20, "L": 5},
           "J":{"M": 30},
           "K":{"M": 50},
           "L":{"K": 20, "M": 10},
           "M":{}}
grafo2 = { "A":{"B": 10, "C": 20},
           "B":{"I": 30, "F": 15},
           "C":{"D": 20, "E": 10},
           "D":{"G": 20, "K": 25},
           "E":{"K": 30},
           "F":{"G": 5, "J": 18},
           "G":{"H": 5},
           "H":{"LR": 30, "M": 30},
           "I":{"J": 20, "O": 26},
           "J":{"O": 28, "LR": 22},
           "K":{"M": 15, "N": 15},
           "LR":{"RR": 32, "Q": 40},
           "M":{"Q": 29, "PR": 10},
           "N":{"PR": 10},
           "O":{"S":22, "RR": 19},
           "PR":{"T": 27, "U": 35},
           "Q":{"X": 18, "T": 19},
           "RR":{"X": 21, "Y": 27},
           "S":{"W": 25, "Y": 36},
           "T":{"Bb": 23, "V": 21},
           "U":{"V":32},
           "V":{"Cc": 15, "Dd": 50},
           "X":{"Aa":16, "Bb": 15},
           "Y":{"Z": 40, "Aa":12, "FfR": 10},
           "W":{"Z": 21},
           "Z":{"Gg": 12},
           "Aa":{"FfR": 16},
           "Bb":{"FfR": 10, "Cc": 19},
           "Cc":{"Ee": 7},
           "Dd":{"Ii": 15},
           "Ee":{"Hh": 20, "Dd": 10},
           "FfR":{"Gg": 15, "Ee": 18},
           "Gg":{"Hh": 10},
           "Hh":{"Ii": 10},
           "Ii":{}
           }

grafo_nao_direcionado = { "A":{"B": 10, "C": 20},
           "B":{"I": 30, "F": 15, "A": 10},
           "C":{"D": 20, "E": 10, "A": 20},
           "D":{"G": 20, "K": 25, "C": 20},
           "E":{"K": 30, "C": 10},
           "F":{"G": 5, "J": 18, "B": 15},
           "G":{"H": 5, "F": 5},
           "H":{"LR": 30, "M": 30, "G": 5},
           "I":{"J": 20, "O": 26, "B": 30},
           "J":{"O": 28, "LR": 22, "F": 18, "I": 20},
           "K":{"M": 15, "N": 15, "D": 25, "E": 30},
           "LR":{"RR": 32, "Q": 40},
           "M":{"Q": 29, "PR": 10},
           "N":{"PR": 10},
           "O":{"S":22, "RR": 19},
           "PR":{"T": 27, "U": 35},
           "Q":{"X": 18, "T": 19},
           "RR":{"X": 21, "Y": 27},
           "S":{"W": 25, "Y": 36},
           "T":{"Bb": 23, "V": 21},
           "U":{"V":32},
           "V":{"Cc": 15, "Dd": 50},
           "X":{"Aa":16, "Bb": 15},
           "Y":{"Z": 40, "Aa":12, "FfR": 10},
           "W":{"Z": 21},
           "Z":{"Gg": 12},
           "Aa":{"FfR": 16},
           "Bb":{"FfR": 10, "Cc": 19},
           "Cc":{"Ee": 7},
           "Dd":{"Ii": 15},
           "Ee":{"Hh": 20, "Dd": 10},
           "FfR":{"Gg": 15, "Ee": 18},
           "Gg":{"Hh": 10},
           "Hh":{"Ii": 10},
           "Ii":{}
           }

def printPath(distancias, inicio, fim):
    if fim != inicio:
        return "%s -- > %s" % (printPath(distancias, inicio, distancias[fim][1]), fim)
    else:
        return inicio

def dijkstra_path(grafo, origem, fim):  # retorna a menor distancia de um No origem até um No destino e o caminho até ele
    controle = {}
    distanciaAtual = {}
    noAtual = {}
    naoVisitados = []
    atual = origem
    noAtual[atual] = 0

    for vertice in grafo.keys():
        naoVisitados.append(vertice)  # inclui os vertices nos não visitados
        distanciaAtual[vertice] = float('inf')  # inicia os vertices como infinito


    distanciaAtual[atual] = [0, origem]
    naoVisitados.remove(atual)

    while naoVisitados:
        for vizinho, peso in grafo[atual].items():
            pesoCalc = peso + noAtual[atual]

            if distanciaAtual[vizinho] == float("inf") or distanciaAtual[vizinho][0] > pesoCalc:
                distanciaAtual[vizinho] = [pesoCalc, atual]
                controle[vizinho] = pesoCalc
        if controle == {}:
            break
        minVizinho = min(controle.items(), key=lambda x: x[1])  # seleciona o menor vizinho
        atual = minVizinho[0]
        noAtual[atual] = minVizinho[1]
        naoVisitados.remove(atual)
        del controle[atual]
    return distanciaAtual[fim][0], printPath(distanciaAtual, origem, fim)

def dijkstra(grafo, origem, fim):  # retorna a menor distancia de um dado nó para todos os outros possíveis.
    carga = 100
    controle = {}
    distanciaAtual = {}
    noAtual = {}
    naoVisitados = []
    atual = origem
    noAtual[atual] = 0

    for vertice in grafo.keys():
        naoVisitados.append(vertice)  # inclui os vertices nos não visitados
        distanciaAtual[vertice] = float('inf')  # inicia os vertices como infinito

    distanciaAtual[atual] = 0
    naoVisitados.remove(atual)

    while naoVisitados:
        for vizinho, peso in grafo[atual].items():
            pesoCalc = peso + noAtual[atual]
            if distanciaAtual[vizinho] == float("inf") or distanciaAtual[vizinho] > pesoCalc:
                distanciaAtual[vizinho] = pesoCalc
                controle[vizinho] = distanciaAtual[vizinho]

        if controle == {}:
            break
        minVizinho = min(controle.items(), key=lambda x: x[1])  # seleciona o menor vizinho
        atual = minVizinho[0]
        noAtual[atual] = minVizinho[1]
        naoVisitados.remove(atual)
        del controle[atual]

    return distanciaAtual


def calculaCaminho(grafo, origem, fim):
    carga = 100
    distanciaAtual = dijkstra(grafo, origem, fim)
    carga_necessaria = distanciaAtual[fim] - 100
    print(carga_necessaria)
    calculated_path = ""
    gasto_total = 0

    if(dijkstra_path(grafo, origem, fim)[0] < carga):
        calculated_path += str(dijkstra_path(grafo, origem, fim)[1])
        print("Carga Suficiente!")
        print(calculated_path)
    else:
        maior_custo_pre_recarga = 0
        while dijkstra_path(grafo, origem, fim)[0] > 100:
            inicio_aux = ""
            for vertices in distanciaAtual:
                if "R" in vertices and dijkstra_path(grafo, origem, vertices)[0] < 100:
                    if maior_custo_pre_recarga < dijkstra_path(grafo, origem, vertices)[0]:
                        maior_custo_pre_recarga = dijkstra_path(grafo, origem, vertices)[0]
                        calculated_path = str(dijkstra_path(grafo, origem, vertices)[1]) + " "
                        gasto_total = dijkstra_path(grafo, origem, vertices)[0]
                        inicio_aux = str(vertices)

            if dijkstra_path(grafo, inicio_aux, fim)[0] < 100:
                calculated_path += " Recarregou " + str(dijkstra_path(grafo, inicio_aux, fim)[1])
                gasto_total += dijkstra_path(grafo, inicio_aux, fim)[0]
                print(calculated_path)
                print(gasto_total)
                break
            else:
                distanciaAtual = dijkstra(grafo, inicio_aux, fim)
                print(dijkstra_path(grafo, inicio_aux, fim))
                print(distanciaAtual)




calculaCaminho(grafo2, "A", "Ii")


