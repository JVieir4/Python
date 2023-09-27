'''
Implemente uma função que calcula o número mínimo de nós de um grafo 
não orientado que cobrem todas as arestas, ou seja, o tamanho do menor 
conjunto de nós que contém pelo menos um extremo de cada aresta. 
A função recebe a lista de todas as arestas do grafo, sendo cada aresta um 
par de nós.
'''


# testa se o candidato c está completo
def complete(p,c,i):
    return len(c) == i

# enumera as extensões válidas para o candidato parcial c
def extensions(p,c,g):
    if len(c) == 0:
        return p
    else:
        return filter(lambda x: x>=c[-1], p)

# testa se um candidato c é uma solução válida para p
def valid(p,c,g):
    for a,b in g:
        if a not in c and b not in c:
            return False
    return True

def aux(p,c,i,g):
    if complete(p,c,i):
        return valid(p,c,g)
    for x in extensions(p,c,g):
        c.append(x)
        if aux(p,c,i,g):
            return True
        c.pop()
    return False

def cobertura(arestas):
    grafo = {}
    for a,b in arestas:
        if a not in grafo:
            grafo[a] = set()
        if b not in grafo:
            grafo[b] = set()
        grafo[a].add(b)
    for i in range(0, len(grafo.keys())+1):
        if aux(sorted(list(grafo.keys())),[],i,arestas):
            return i
        
def main():
    print("<h3>cobertura</h3>")
    arestas = [('portugal','espanha'),('espanha','franca'),('franca','alemanha'),('alemanha','belgica'),('belgica','franca'),('usa','canada'),('usa','mexico'),('marrocos','argelia'),('argelia','libia'),('argelia','mali')]
    print("in:",arestas)
    print("out:",cobertura(arestas))

import unittest

class coberturaTest(unittest.TestCase):

    def test_cobertura_1(self):
            arestas = [('portugal','espanha'),('espanha','franca'),('franca','alemanha'),('alemanha','belgica'),('belgica','franca'),('usa','canada'),('usa','mexico'),('marrocos','argelia'),('argelia','libia'),('argelia','mali')]
            self.assertEqual(cobertura(arestas),5)

    def test_cobertura_2(self):
            arestas = [('a','b'),('b','c'),('c','d'),('d','e'),('e','f'),('f','g'),('g','h')]
            self.assertEqual(cobertura(arestas),4)
          
            
if __name__ == '__main__':
    main()
    unittest.main()