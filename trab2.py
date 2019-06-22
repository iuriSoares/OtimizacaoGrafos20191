import json
import random

g = json.load(open('data3.json'))

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

def vizinhos(grafo,v):
    v = str(v)
    vizinhos = []
    arestas = grafo["arestas"]
    for par in arestas:
        if(par.count(v) > 0):
            for x in par :
                if(x != v):
                    vizinhos.append(str(x))
                    
    return vizinhos


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
    countExplo = 0 #arestas exploradas
    tamViz = len(vizinhos(grafo, raiz+1)) #quantidade de vizinhos
    visitado[int(raiz)] = True
    while countExplo != len(grafo["arestas"]) and tamViz != 0:
            #vw = random.choice(grafo["arestas"]) #escolhe aresta aleatoriamente
        for vw in g["arestas"]:
            if visitado[int(vw[0]) - 1] or visitado[int(vw[1]) - 1]:
                if not explorada[int(vw[0]) - 1][int(vw[1]) - 1] or not explorada[int(vw[1]) - 1][int(vw[0]) - 1]:
                    countExplo += 1
                    explorada[int(vw[0]) - 1][int(vw[1]) - 1] = True
                    explorada[int(vw[1]) - 1][int(vw[0]) - 1] = True
                    if not visitado[int(vw[1]) - 1] or not visitado[int(vw[0]) - 1]:
                        visitado[int(vw[0]) -1], visitado[int(vw[1]) -1], descoberta[int(vw[0]) - 1][int(vw[1]) - 1], descoberta[int(vw[1]) - 1][int(vw[0]) - 1] = True, True, True, True

                    
def BuscaCompleta (grafo):
    for i in range (len(grafo["vertices"])):
        if not visitado[i]:
            Busca(grafo,i)
            

def EhConexo(grafo):
    Busca(grafo,0)
    for v in grafo["vertices"]:
        if not visitado[int(v) - 1]:
            return False
    return True


def TemCiclo(grafo):
    BuscaCompleta(grafo)
    for uv in grafo["arestas"]:
        if not descoberta[int(uv[0]) - 1][int(uv[1]) - 1] or not descoberta[int(uv[1]) - 1][int(uv[0]) - 1]:
                return True
    return False


def EhFloresta(grafo):
    return not TemCiclo(grafo)


def EhArvore(grafo):
    Busca(grafo,0)
    for v in grafo["vertices"]:
        if not visitado[int(v)-1]:
            return False

    for uv in grafo["arestas"]:
        if not descoberta[int(uv[0]) - 1][int(uv[1]) - 1] or not descoberta[int(uv[1]) - 1][int(uv[0]) - 1]:
            return False
    return True


def EhArvore2(grafo):
    return (EhConexo(grafo) and not TemCiclo(grafo))



def ObterFlorestaGeradora(grafo):
    T = grafo
    vertices = grafo["vertices"]
    arestas = []
    BuscaCompleta(grafo)
    for uv in grafo["arestas"]:
        if descoberta[int(uv[0]) - 1][int(uv[1]) - 1] or descoberta[int(uv[1]) - 1][int(uv[0]) - 1]:
            arestas.append(uv)
    T["arestas"] = []
    T["arestas"] = arestas
    return T


#FALTA TESTAR
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


#FALTA TESTAR
def BuscaProfundidade2(grafo, vertice):
    visitado[vertice] = True
    for vizinho in grafo["vertices"][vertice]:
        if visitado[vizinho]:
            if not explorada[vertice][vizinho]:
                explorada[vertice][vizinho] = True
        else:
            explorada[vertice][vizinho],descoberta[vertice][vizinho] = True, True
            BuscaProfundidade2(grafo, vizinho)


#FALTA TESTAR
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
                
#FALTA TESTAR
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

def Dijkstra(grafo, s):
    
    w = [] #Lista de peso das arestas
    linha = []
    rd = 0 #valor do radom
    
    for i in range (len(g["vertices"])):
        for j in range (len(g["vertices"])):
            linha.append(None)
        w.append(linha)
        linha = []

    for vw in grafo["arestas"]:#Preenchendo com pesos aleatorios
        rd = random.random() * 100
        w[int(vw[0]) - 1][int(vw[1]) - 1] = rd
        w[int(vw[1]) - 1][int(vw[0]) - 1] = rd

    #print(w)

    d = [float('inf')]*len(grafo["vertices"]) #Distancia entre o start e o vertice
    T = [False]*len(grafo["vertices"]) #Caminho minimo entre v e start
    P = [None]*len(grafo["vertices"]) #Menor caminho entre v e start
    d[s-1] = 0
    
    for i in grafo["vertices"]:
            if not T[int(i)-1]:
                u = int(i)-1
                T[u] = True
                for v in vizinhos(grafo, (u+1)):
                    if d[int(v) - 1] > (w[int(v) - 1][u]+d[u]):
                        d[int(v) - 1] = (w[int(v) - 1][u]+d[u])
                        P[int(v) - 1] = (u+1)
    return d, P
    
print(Dijkstra(g, 1))


import time
inicio = time.time()
#JOGAR FUNCAO AQUI
fim = time.time()
#print(fim - inicio)
