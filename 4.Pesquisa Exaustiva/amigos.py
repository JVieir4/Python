'''
Implemente uma função que descubra o maior conjunto de pessoas que se conhece 
mutuamente. A função recebe receber uma sequências de pares de pessoas que se 
conhecem e deverá devolver o tamanho do maior conjunto de pessoas em que todos 
conhecem todos os outros.
'''

# testa se o candidato c está completo
def complete(p,c,k):
    return len(c) == k


# enumera as extensões válidas para o candidato parcial c
def extensions(p,c,l,g):
    if len(c) == 0:
        return l
    else:
        r = list()
        for new in filter(lambda x: x>c[-1], l):
            for old in c:
                if new not in g[old] or old not in g[new]:
                    break
            else:
                r.append(new)
        return r


# testa se um candidato c é uma solução válida para p
def valid(p,c):
    return True


def aux(p,c,k,l,g):
    if complete(p,c,k):
        return valid(p,c)
    for x in extensions(p,c,l,g):
        c.append(x)
        if aux(p,c,k,l,g):
            return True
        c.pop()
    return False


def amigos(conhecidos):
    grafo = {}
    for x,y in conhecidos:
        if x not in grafo:
            grafo[x] = set()
        if y not in grafo:
            grafo[y] = set()
        grafo[x].add(y)
        grafo[y].add(x)
    
    for i in range(len(grafo.keys()), 0, -1):
        c = []
        if aux(conhecidos, c, i, (list(grafo.keys())), grafo):
            return i
    return 0

def main():
    print("<h3>amigos</h3>")
    conhecidos = {('pedro','maria'),('pedro','jose'),('pedro','manuel'),('maria','jose'),('maria','francisca'),('jose','francisca'),('francisca','manuel')}
    print("in:",conhecidos)
    print("out:",amigos(conhecidos))
    
import unittest

class amigosTest(unittest.TestCase):
    def test_amigos_1(self):
            conhecidos = {('pedro','maria'),('pedro','jose'),('pedro','manuel'),('maria','jose'),('maria','francisca'),('jose','francisca'),('francisca','manuel')}
            self.assertEqual(amigos(conhecidos),3)
            
    def test_amigos_2(self):
            conhecidos = {('pedro','maria'),('jose','francisca'),('manuel','pedro')}
            self.assertEqual(amigos(conhecidos),2)
          
            
if __name__ == '__main__':
    main()
    unittest.main()
