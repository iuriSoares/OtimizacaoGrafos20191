import json
import random

#CAMINHOS MINIMOS

#carrega o grafo atraves do arquivo Json
g = json.load(open('data5.json'))

#retorna os vizinhos do vertice solicitado no grafo
def vizinhos(grafo,v):
    v = str(v)
    vizinhos = []
    arestas = grafo["arestas"]
    for par in arestas: #par percorre as arestas
        if(par.count(v) > 0): #se contem o vertice v em alguma das arestas
            for x in par : #x percorre par
                if(x != v): #se x e diferente de v significa que ele e vizinho de v
                    vizinhos.append(str(x)) #insere x       
    return vizinhos


def CaminhoMinimo(grafo, s):
  #Funcao criada utilizando o algoritmo Dijkstra
	
  w = [] #lista de peso das arestas
  rd = 0 #valor do radom
  linha = [] #linha vazia para preencher a lista de peso das arestas
    
  #preenchendo a matriz de pesos com valores nulos
  for i in range (len(grafo["vertices"])):
      for j in range (len(grafo["vertices"])):
          linha.append(None)
      w.append(linha) 
      linha = []

  for vw in grafo["arestas"]:#preenchendo a listas de pesos com pesos aleatorios para as arestas existentes
      rd = random.random() * 100 #gerando numero aleatorio entre 0 e 100
      w[int(vw[0]) - 1][int(vw[1]) - 1] = rd #insere numero aleatorio
      w[int(vw[1]) - 1][int(vw[0]) - 1] = rd #insere numero aleatorio

  d = [float('inf')]*len(grafo["vertices"]) #distancia entre o start e o v
  T = [False]*len(grafo["vertices"]) #caminho minimo entre v e start
  P = [None]*len(grafo["vertices"]) #menor caminho entre v e start
  d[s-1] = 0
    
  for i in grafo["vertices"]: #percorre vertices do grafo
          if not T[int(i)-1]: #n�o T[v]
              u = int(i)-1
              T[u] = True #T[u] = V
              for v in vizinhos(grafo, (u+1)): #percorre os vizinhos de v
                  if d[int(v) - 1] > (w[int(v) - 1][u]+d[u]): #se distancia entre s e v e maior que w(xy)+d(y,s)
                      d[int(v) - 1] = (w[int(v) - 1][u]+d[u]) #d[v] recebe w[vu]+d[u]
                      P[int(v) - 1] = (u+1)
  return d, P
  
    
#Marcando Tempos
import time
inicio = time.time()
CaminhoMinimo(g, 1) #Iniciando do vertice 1
fim = time.time()
print ('duracao: %0.9f' % (fim - inicio))
