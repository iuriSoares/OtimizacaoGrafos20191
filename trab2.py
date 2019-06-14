print ("Hello Word")
import json

g = json.load(open('data10.json'))

explorada = []
descoberta = []
linha1 = []
linha2 = []
visitado = [False] * len(g["vertices"])

#cria explorada e descoberta
for i in range (len(g["vertices"])):
    for j in range (len(g["vertices"])):
        linha1.append(False)
        linha2.append(False)
    explorada.append(linha1)
    descoberta.append(linha2)
    linha1 = []
    linha2 = []


def rotula(a):

    if not(visitado[a]):

        visitado[a] = True


def geraListaAdjacencia(grafo):
    vertices = grafo["vertices"] 	
    arestas = grafo["arestas"] 
    lista = [] 

    for i in vertices: 		
        aux = [] 
        for j in arestas: 
            if i in j: 
                if (i == j[0]): 					
                    aux.append(int(j[1]))
                else: 					
                    aux.append(int(j[0]))
        lista.append(aux) 
     
    return lista 



def Busca(grafo, raiz):

    lista = geraListaAdjacencia(grafo)
    visitado[int(raiz)] = True
    for i in range(len(lista)):
        if visitado[i]:
            for vizinho in lista[i]:
                vizinho -= 1
                if not explorada[i][vizinho]:
                    explorada[i][vizinho] = True
                    if not visitado[vizinho]:
                        visitado[vizinho] = True
                        descoberta[i][vizinho] = True

                    
def BuscaCompleta (grafo):

    for i in range (len(grafo["vertices"])):
        if not visitado[i]:
            Busca(grafo,i)

    print(visitado)
    print(explorada)
    print(descoberta)





def EhConexo(grafo):

    Busca(grafo,0)

    for i in grafo["vertices"]:

        if not visitado[int(i)]:

            return False

    return True





def TemCiclo(grafo):

    BuscaCompleta(grafo)

    for i in range (grafo["vertices"]):

        for j in range (grafo["arestas"]):

            if not descoberta[i][j]:

                return True

    return False





def EhFloresta(grafo):

    return not TemCiclo(grafo)





def EhArvore(grafo):

    Busca(grafo,0)

    for k in grafo["vertices"]:

        if not visitado[k]:

            return True



    for i in range (grafo["vertices"]):

        for j in range (grafo["arestas"]):

            if not descoberta[i][j]:

                return False



    return True





def EhArvore2(grafo):

    return (EhConexo(grafo) and not TemCiclo(grafo))



def ObterFlorestaGeradora(grafo):

    verticesT = grafo["vertices"]

    arestasT = []



    BuscaCompleta(grafo)



    for i in grafo["vertices"]:

        for j in grafo["arestas"]:

            if descoberta[i][j]:

                arestasT.append([i,j])

    return verticesT, arestasT



def BuscaProfundidade(grafo, vertice):



    def PrimeiroVizinho(vertice):

        try:

            return int(grafo["arestas"][vertice][0])

        except:

            return 0



    def ProximoVizinho(vertice, vizinho):

        try:

            return int(grafo["arestas"][vertice][vizinho+1])

        except:

            return 0



    pilha = []

    visitado[vertice] = True

    tupla = (vertice, PrimeiroVizinho(vertice))

    pilha.append(tupla)



    while (len(pilha) > 0) :

        tupla = pilha.pop()

        

        if (tupla[1] > 0):

            vizinho = tupla[1]

            tuplaAux = (vertice, ProximoVizinho(vertice, vizinho))

            pilha.append(tuplaAux)



            if (visitado[vizinho]):

                if not explorada[vertice][vizinho]:

                    explorada[vertice][vizinho] = True

            else:

                explorada[vertice][vizinho] = True

                descoberta[vertice][vizinho]  = True

                visitado[vizinho] = True

                pilha.append(vizinho, PrimeiroVizinho(vizinho))    

    return pilha



def BuscaProfundidade2(grafo, vertice):

    visitado[vertice] = True

    for vizinho in grafo["vertices"][vertice]:

        if visitado[vizinho]:

            if not explorada[vertice][vizinho]:

                explorada[vertice][vizinho] = True

        else:

            explorada[vertice][vizinho],descoberta[vertice][vizinho] = True, True

            BuscaProfundidade2(grafo, vizinho)



def BuscaLargura(grafo, vertice):

    fila = []

    visitado[vertice] = True

    fila.append(vertice)

    while (len(fila) > 0):

        verticeAux = fila.pop(0)

        for vizinho in grafo["vertices"][vertice]:

            if visitado[vizinho]:

                if not explorada[vertice][vizinho]:

                    explorada[vertice][vizinho] = True

            else:

                explorada[vertice][vizinho],descoberta[vertice][vizinho] = True, True

                visitado[vizinho] = True

                fila.append(vizinho)



def DeterminarDistancias(grafo, vertice):

    fila = []

    distancia = [float('inf')]*len(grafo["vertices"])

    fila.append(vertice,1)

    while len(fila) > 0:

        tupla = fila.pop(0)

        for vizinho in grafo["vertices"]:

            if visitado[vizinho]:

                if not visitado[vertice][vizinho]:

                    explorada[vertice][vizinho] = True

            else:

                explorada[vertice][vizinho],descoberta[vertice][vizinho] = True, True

                niv = tupla[1]

                visitado[vizinho], distancia[vizinho] = True, niv

                tuplaAux = (vizinho, niv+1)

                fila.append(tuplaAux)






import time

inicio = time.time()
EhConexo(g)
fim = time.time()
print(fim - inicio)
