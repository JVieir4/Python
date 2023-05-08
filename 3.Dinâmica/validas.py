"""
Um exemplo de um problema que pode ser resolvido de forma eficiente com 
programação dinâmica consiste em determinar, dada uma sequência arbitrária de 
números não negativos, se existe uma sub-sequência (não necessariamente contígua) 
cuja soma é um determinado valor. Implemente uma função que dado um valor e uma
listas de listas de números não negativos, devolva a lista com as listas com uma
sub-sequência cuja soma é o valor dado.
"""


def aux(sum,lst):
    conjunto = {0}
    for i in lst:
        aux = set()
        for e in conjunto:
            aux.add(e+i)
        conjunto = conjunto | aux
    return sum in conjunto
    

def validas(soma,listas):
    res = []
    for lista in listas:
        if aux(soma,lista):
           res.append(lista) 
    
    return res

def main():
    print("<h3>validas</h3>")
    listas = [[8,1,7,3,3,6,3,5],[1,1,1,2,3,1,2],[3,3,3,3]]
    print("in:",10,listas)
    print("out:",validas(10,listas))
    
import unittest

class validasTest(unittest.TestCase):
    
    def test_validas_1(self):
            listas = [[8,1,7,3,3,6,3,5],[1,1,1,2,3,1,2],[3,3,3,3]]
            self.assertEqual(validas(10,listas),[[8,1,7,3,3,6,3,5],[1,1,1,2,3,1,2]])

    def test_validas_2(self):
            listas = [[1,1,1,1,1],[2],[3,3,3,3,3,3,3],[4],[5,5,5,5,5]]
            self.assertEqual(validas(5,listas),[[1,1,1,1,1],[5,5,5,5,5]])
          
            
if __name__ == '__main__':
    main()
    #unittest.main()