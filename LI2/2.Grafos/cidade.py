'''

Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que calcula o tamanho de uma cidade, 
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os 
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a 
letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

'''

def build(ruas):
    adj = {}
    for rua in ruas:
        c1 = rua[0]
        c2 = rua[-1]
        if c1 not in adj:
            adj[c1] = {}
        if c2 not in adj:
            adj[c2] = {}
        if c2 in adj[c1] and adj[c1][c2] < len(rua):
            continue
        adj[c1][c2] = len(rua)
        adj[c2][c1] = len(rua)
    #print(adj)
    return adj

def fw(adj):
    dist = {}
    for o in adj:
        dist[o] = {}                # para cada vértice do grafo coloca-se o dicionário vazio
        for d in adj:
            if o == d:                  # se os vértices "o" e "d" forem iguais
                dist[o][d] = 0          # coloca-se a distância a 0
            elif d in adj[o]:                   # se os vértices "o" e "d" forem adjacentes
                dist[o][d] = adj[o][d]          # inicializam-se com o peso da sua aresta conectora
            else:                                       # se não forem adjacentes
                dist[o][d] = float("inf")               # inicializam-se temporariamente como infintos
    for k in adj:
        for o in adj:                                           # o que essencialmente está a acontecer neste triplo ciclo é que
            for d in adj:                                       # para calcular a distância mais curta entre "o" e "d",
                if dist[o][k] + dist[k][d] < dist[o][d]:        # testa-se exaustivamente todas as possibilidades de
                    dist[o][d] = dist[o][k] + dist[k][d]        # vértices intermédios até chegar-mos á melhor estimativa
    print(dist)
    return dist

def tamanho(ruas):
    adj = build(ruas)
    print(adj)
    dist = fw(adj)
    final = 0
    for i in adj:
        for k in adj:
            final = max(final, dist[i][k])
    return final

def main():
    print("<h3>tamanho</h3>")
    ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]
    print("in:", ruas)
    print("out:", tamanho(ruas))
    
import unittest

class tamanhoTest(unittest.TestCase):
    
    def test_tamanho_1(self):
            ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]
            self.assertEqual(tamanho(ruas),25)

    def test_tamanho_2(self):
            ruas = ["ab","bc","bd","cd"]
            self.assertEqual(tamanho(ruas),4)
            
            
if __name__ == '__main__':
    main()
    #unittest.main()