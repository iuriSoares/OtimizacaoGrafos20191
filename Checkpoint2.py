import json

#carrega o grafo atraves do arquivo Json
g = json.load(open('data3.json'))

#inicia as variaveis
explorada = []
descoberta = []
visitado = [False] * len(g["vertices"])
linha1 = []
linha2 = []

#criacao das matrizes explorada e descoberta com False
for i in range (len(g["vertices"])):
    for j in range (len(g["vertices"])):
        linha1.append(False)
        linha2.append(False)
    explorada.append(linha1)
    descoberta.append(linha2)
    linha1 = []
    linha2 = []

#retorna os vizinhos do vertice solicitado no grafo
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

def existe(grafo): #enquanto existir vertice visitado com aresta nao explorada
  for a in grafo["vertices"]: #percorre vertices
    if visitado[int(a) - 1]: #verifica se foi visitado
      for b in vizinhos(grafo, int(a)): #percorre vizinhos
        if not explorada[int(b)-1][int(a) - 1]: #verifica se vizinho nao foi explorado
          return True
  return False

def Busca(grafo, raiz):
    visitado[int(raiz)-1] = True #coloca como visitado o vertice raiz vindo do parametro da funcao
	
    while existe(grafo):
        for vw in grafo["arestas"]:#percorre arestas
            if visitado[int(vw[0]) - 1] or visitado[int(vw[1]) - 1]:#se um dos dois vertices que compoem a aresta foram visitados
                if not explorada[int(vw[0]) - 1][int(vw[1]) - 1] or not explorada[int(vw[1]) - 1][int(vw[0]) - 1]:#e entre eles nao tiver aresta explorada
                    explorada[int(vw[0]) - 1][int(vw[1]) - 1] = True
                    explorada[int(vw[1]) - 1][int(vw[0]) - 1] = True
                    if not visitado[int(vw[1]) - 1] or not visitado[int(vw[0]) - 1]:#se o outro vertice nao tiver sido visitado
                        visitado[int(vw[0]) - 1], visitado[int(vw[1]) - 1], descoberta[int(vw[0]) - 1][int(vw[1]) - 1], descoberta[int(vw[1]) - 1][int(vw[0]) - 1] = True, True, True, True

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


#Função que realiza a busca em profundidade
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
        v,w = pilha.pop()
        if (w > 0):
            tuplaAux = (v, ProximoVizinho(v, w))
            pilha.append(tuplaAux)
            if (visitado[w]):
                if not explorada[v][w]:
                    explorada[v][w] = True
            else:
                explorada[v][w] = True
                descoberta[v][w]  = True
                visitado[w] = True
                aux = (w, PrimeiroVizinho(w)) #auxiliar para criar tupla
                pilha.append(aux)    
    return pilha


#Função que realiza a busca em profundidade recusiva
def BuscaProfundidade2(grafo, vertice):
    visitado[int(vertice)-1] = True
    for vizinho in grafo["vertices"][int(vertice)]:
        if visitado[int(vizinho)-1]:
            if not explorada[int(vertice)-1][int(vizinho)-1]:
                explorada[int(vertice)-1][int(vizinho)-1] = True
        else:
            explorada[int(vertice)-1][int(vizinho)-1],descoberta[int(vertice)-1][int(vizinho)-1] = True, True
            BuscaProfundidade2(grafo, vizinho)


#Busca em largura
def BuscaLargura(grafo, vertice):
    fila = []
    visitado[vertice] = True
    listaAdjacencia = geraListaAdjacencia(grafo)
    fila.append(vertice)

    while (len(fila) > 0):
        v = fila.pop(0)
        for w in listaAdjacencia[v]:
            w -= 1
            if visitado[w]:
                if not explorada[v][w]:
                    explorada[v][w] = True
            else:
                explorada[v][w], descoberta[v][w] = True, True
                visitado[w] = True
                fila.insert(0,w)
#Função apra determinaar a distancia
def DeterminarDistancias(grafo, vertice):
    fila = []
    visitado[vertice] = True
    distancia = [float('inf')]*len(grafo["vertices"])
    listaAdjacencia = geraListaAdjacencia(grafo)
    fila.insert(0,(vertice,1))
    while len(fila) > 0:
        v, niv = fila.pop(0)
        for w in listaAdjacencia[v]:
            w -= 1 
            if visitado[w]:
                if not explorada[v][w]:
                    explorada[v][w] = True
            else:
                explorada[v][w],descoberta[v][w] = True, True
                visitado[w], distancia[w] = True, niv
                tuplaAux = (v, niv+1)
                fila.insert(0,tuplaAux)
    print(distancia)


#import time
#inicio = time.time()
#Inserir Funcao aqui DeterminarDistancias(g,1)
#fim = time.time()
#print('%0.19f' % (fim - inicio))

  