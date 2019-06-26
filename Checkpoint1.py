import json

g = json.load(open('teste.json'))

#Cria o vertice recebido no parametro caso nao exista no grafo
def addVert(grafo,a):
    vertices = grafo["vertices"]
    if(vertices.count(str(a)) == 0):
        vertices.append(str(a))
        grafo["vertices"] = vertices
    return grafo

#Cria uma aresta entre os dois vertices recebidos nos parametros caso nao exista no grafo
def addAre(grafo,a,b):
    c = []
    arestas = grafo["arestas"]
    if(vertices.count(str(a)) > 0 and vertices.count(str(b)) > 0):
        c.append(str(a))
        c.append(str(b))
        arestas.append(c)
        grafo["arestas"] = arestas
    return grafo
    
#Remove uma aresta entre os dois vertices recebidos nos parametros caso exista no grafo
def delAre(grafo,a,b):
    c = []
    d = []
    c.append(str(a))
    c.append(str(b))
    d.append(str(b))
    d.append(str(a))
    arestas = grafo["arestas"]
    if(arestas.count(c) > 0):   
        arestas.remove(c)
    elif arestas.count(d) > 0:
        arestas.remove(d)
    grafo["arestas"] = arestas
    return grafo
    
#Retorna uma lista de vizinhos do vertice recebido no parametro caso ele exista no grafo
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

#Remove o vertice recebido no parametro caso exista no grafo    
def delVert(grafo,a):
    vertices = grafo["vertices"]
    if(vertices.count(str(a)) > 0):
        vertices.remove(str(a))
        grafo["vertices"] = vertices
        arestas = grafo["arestas"]
        for x in vizinhos(grafo, a):
            delAre(grafo,x,a)
            grafo["arestas"] = arestas

    return grafo

def GerarMatrizAdjacencia(grafo):
    n = len(grafo["vertices"])
    m = len(grafo["arestas"])
    M = []
    for i in range(n):
        M.append([0]*n)
    for i in range(m):
        u = grafo["arestas"][i-1][0]
        v = grafo["arestas"][i-1][1]

        a = int(u)-1
        b = int(v)-1

        M[a][b] = 1
        M[b][a] = 1
        
    return M

def geraListaAdjacencia(grafo):
	vertices = grafo["vertices"]
	arestas = grafo["arestas"]
	lista = []

	for i in vertices:
		aux = []
		for j in arestas:
			if i in j:
				if (i == j[0]):
					aux.append(j[1])
				else:
					aux.append(j[0])
		lista.append(aux)
		
	return lista
    



print("Matriz Adjacencia: \n")
M = GerarMatrizAdjacencia(g)
n = len(g["vertices"])
for i in range(n):
    for j in range(n):
        print(M[i][j], end="")
    print("\n")
print("==============================================================================")
print("Lista Adjacencia: \n")
L = geraListaAdjacencia(g)
m = len(geraListaAdjacencia(g))
for i in range(m):
    print(L[i], "\n")
    



